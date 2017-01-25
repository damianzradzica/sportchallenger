$(document).ready(function() {

    var $days = $('.days').find('li').find('button');

    $days.one('click', function() {
            $(this).toggleClass('clicked');
        });

    var pathname = window.location.pathname.split("/");
    var filename = pathname[pathname.length-1]; // przechowuje ID obiektu

    $.ajax({url: "http://127.0.0.1:8000/reservationlist"}).done(function(json) {
        var list = [] //zmienna przechowuje daty, dla których w danym obiekcie już dokonano rezerwacji
        for (i=0; i<json.length; i++) {
            if (json[i].facility == filename) {
                var temp = json[i].reservation_date;
                var date_format = moment(temp).format("YYYY-MM-DD");
                list.push(date_format);
            }
        };
        console.log(list);
        var $date = $('.days').find('li').find('button');
        $date.each(function() {
            var temporary = new Date($(this).find('a').text()); //wyszukuje tekst w tagu a
            var date_ready = moment(temporary).format("YYYY-MM-DD"); //zamienia wyszukany tekst na sformatowaną datę
            if (list.indexOf(date_ready) > -1) {
                $(this).toggleClass('unavailable'); //dla dat, które nie są dostępne, buttonów nie można wybrać
            }
        });
    });
});

//$.ajax({url: "http://127.0.0.1:8000/reservationlist"}).done(function(json) {
// Ważne info!!! Dana z ajaxa są zapisane w zmiennej json(argument funkcji done powyżej). Na tej zmiennej
// pracujemy żeby uzyskać dane
