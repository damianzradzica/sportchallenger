from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import FormView
from django.views.generic import UpdateView
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from sportchallenger.forms import LoginForm, MonthForm, ReservationForm, NewUserForm
from sportchallenger.models import Reservation, SportFacility, KINDS, SPORTS, MyUser
from sportchallenger.serializers import ReservationSerializer, FacilitySerializer

# Create your views here.



class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "sportchallenger/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():  # dopiero jak zrobimy walidację to utworzy się słownik cleaned_data
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username=u, password=p)

        if user is not None:
            login(request, user)
            return redirect('main_page')
        else:
            raise ValidationError('Błędny login lub hasło')

class MainView(View):
    def get(self, request):
        facilities = SportFacility.objects.all()
        list = []
        user = request.user
        for a in facilities:
            d = dict()
            d['id'] = a.id
            d['name'] = a.name
            d['photos'] = a.photos
            d['kind'] = dict(KINDS).get(a.kind)
            d['city'] = a.city
            d['street'] = a.street
            d['price'] = a.price
            list.append(d)

        return render(request, "sportchallenger/main_page.html", {'facility': list,
                                                                  'user': user })

class FacilityView(LoginRequiredMixin, View):
    def get(self, request, pk):
        facility = SportFacility.objects.get(id = pk)
        form = MonthForm()
        ctx = {
            'facility': facility,
            'kind': dict(KINDS).get(facility.kind),
            'sports': dict(SPORTS).get(facility.sports),
            'photo': facility.photos,
            'form': form
        }
        return render(request, 'sportchallenger/facility_details.html', ctx)
    def post(self, request, pk):
        facility = SportFacility.objects.get(id=pk)
        form = MonthForm(request.POST)
        if form.is_valid():
            month_info = int(form.cleaned_data['month'])
            year = form.cleaned_data['year']

        long_months = (1, 3, 5, 7, 8, 10, 12)
        short_months = (4, 6, 9, 11)

        if month_info in long_months:
            days = 31
        elif month_info in short_months:
            days = 30
        elif month_info ==2:
            if year % 4 == 0:
                days = 29
            else:
                days = 28

        counter = 1
        list = []
        first_day = datetime.date(year, month_info, 1)
        list.append(first_day)

        while counter < days:
            base = first_day + datetime.timedelta(days = 1)
            list.append(base)
            first_day += datetime.timedelta(days = 1)
            counter += 1

        ctx = {
            'year': year,
            'days': days,
            'month': month_info,
            'list': list,
            'facility': facility
        }

        return render(request, 'sportchallenger/2calendar.html', ctx)


class ReservationView(LoginRequiredMixin, View):
    def get(self, request, pk, ryear, rmonth, rday):
        data = SportFacility.objects.get(id = pk)
        facility_form = data.name
        facility_price = data.price
        user = request.user.username
        form = ReservationForm(initial = {
            'facility': facility_form,
            'user': user,
            'reservation_date': '{}/{}/{}'.format(rday, rmonth, ryear),
            'price': facility_price
        })

        ctx = {
            'form': form
        }

        return render(request, "sportchallenger/reservation.html", ctx)

    def post(self, request, pk, ryear, rmonth, rday):
        day = int(rday)
        month = int(rmonth)
        year = int(ryear)
        booking = datetime.date(year, month, day)
        r_number = Reservation.objects.create(reservation_date=booking)
        facility_object = SportFacility.objects.get(id=pk)
        user_object = request.user
        myuser = MyUser.objects.get(user = user_object) #albo get or create jeśli do usera nie ma przypisanego myusera
        r_number.facility = facility_object
        r_number.user = myuser
        r_number.save()

        return render(request, "sportchallenger/thanks.html")

class UserDetailsView(LoginRequiredMixin, View):
    def get(self, request):
        user_object = request.user
        myuser = MyUser.objects.get(user = user_object)
        booking_old = Reservation.objects.all().filter(reservation_date__lt=datetime.date.today()).filter(user = myuser)
        booking_new = Reservation.objects.all().filter(reservation_date__gte=datetime.date.today()).filter(user=myuser)
        print(booking_old)
        ctx = {
            'user': user_object,
            'myuser': myuser,
            'booking_old': booking_old,
            'booking_new': booking_new
        }
        return render(request, "sportchallenger/user_details.html", ctx)

class AddUserView(View):
    def get(self, request):
        base_form = NewUserForm()
        ctx = {
            'base_form': base_form,
        }
        return render(request, "sportchallenger/newuser_form.html", ctx)

    def post(self, request):
        form = NewUserForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            nickname = form.cleaned_data['nickname']
            photo = form.cleaned_data['photo']
            u = User.objects.create_user(username=username, password=password, email = email)
            u.save()
            mu = MyUser.objects.create(user=User.objects.get(username=u.username), nickname=nickname, photo = photo)
            mu.save()
        else:
            return HttpResponse('form is invalid')
        return render(request, "sportchallenger/thanks_user.html")

class LoadReservation(APIView):
    def get(self, request, format = None):
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True, context={'request': request})
        return Response(serializer.data)

class LoadFacility(APIView):
    def get(self, request, format = None):
        facilities = SportFacility.objects.all()
        serializer = FacilitySerializer(facilities, many=True, context={'request': request})
        return Response(serializer.data)

class AddFacilityView(PermissionRequiredMixin, CreateView):
        model = SportFacility
        permission_required = 'sportchallenger.add_sportfacility'
        fields = '__all__'

class UpdateFacilityView(PermissionRequiredMixin, UpdateView):
    model = SportFacility
    permission_required = 'sportchallenger.change_sportfacility'
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('main_page')

class DeleteFacilityView(PermissionRequiredMixin, DeleteView):
    model = SportFacility
    permission_required = 'sportchallenger.delete_sportfacility'
    success_url = reverse_lazy('main_page')