"""reservations URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from sportchallenger.views import LoginView, MainView, FacilityView, ReservationView, UserDetailsView, AddUserView, \
    LoadReservation
from django.contrib import admin
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$', logout_then_login, name='site-logout'),
    url(r'^login$', LoginView.as_view(), name = 'login_page'),
    url(r'^$', MainView.as_view(), name = 'main_page'),
    url(r'^facility/(?P<pk>(\d)+)$', FacilityView.as_view(), name = 'facility_details'),
    url(r'^facility/(?P<pk>(\d)+)/(?P<ryear>(\d)+)/(?P<rmonth>(\d)+)/(?P<rday>(\d)+)$', ReservationView.as_view(), \
        name = 'reservation'),
    url(r'^user$', UserDetailsView.as_view(), name = 'user_details'),
    url(r'^newuser$', AddUserView.as_view(), name = 'new_user'),
    url(r'^reservationlist$', LoadReservation.as_view(), name='reservation_list'),
]
