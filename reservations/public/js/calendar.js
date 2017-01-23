$(document).ready(function() {
// tu nasz kod
var $days = $('.days').find('li').find('button')

});

$days.one('click', function () {
		$(this).toggleClass('clicked');
	});
});

//$.ajax({url: "http://127.0.0.1:8000/reservationlist"}).done(function(json) {
//    var $reservations = $("reservation_date");
////    var $reservations = $.parseJSON()
//    console.log(reservations)