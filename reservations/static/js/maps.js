$(document).ready(function() {
    var streetlist = []; //przechowuje adresy obiektów
    var citylist = []; //przechowuje miasta obiektów
    $.ajax({url: "http://127.0.0.1:8000/facilitieslist"}).done(function(json) {
        for(i=0; i<json.length; i++) {
            streetlist.push(json[i].street);
            citylist.push(json[i].city);
        };
    });
    console.log(streetlist);
    console.log(citylist);

     function initMap() {
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 8,
          center: {lat: -34.397, lng: 150.644}
        });
        var geocoder = new google.maps.Geocoder();

        document.getElementById('submit').addEventListener('click', function() {
            geocodeAddress(geocoder, map);
        });
      }

     function geocodeAddress(geocoder, resultsMap) {
         for(i=0; i<streetlist.length; i++) {
            var address = streetlist[i] + ', ' + citylist[i]
            geocoder.geocode({'address': address}, function(results, status) {
                if (status === 'OK') {
                    resultsMap.setCenter(results[0].geometry.location);
                    var marker = new google.maps.Marker({
                        map: resultsMap,
                        position: results[0].geometry.location
                        });
                } else {
                    alert('Geocode was not successful for the following reason: ' + status);
                }
            });
        };
     };

});