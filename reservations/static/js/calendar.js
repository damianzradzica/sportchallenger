$(document).ready(function() {

var $days = $('.days').find('li').find('button')

});

$days.one('click', function () {
		$(this).toggleClass('clicked');
	});

//$.ajax({url: "http://127.0.0.1:8000/reservationlist"}).done(function(json) {
// Ważne info!!! Dana z ajaxa są zapisane w zmiennej json(argument funkcji w done powyżej). Na tej zmiennej
// pracujemy żeby uzyskać dane
//    var $reservations = $("reservation_date");
////    var $reservations = $.parseJSON()
//    console.log(reservations)