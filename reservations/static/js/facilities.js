$(document).ready(function() {

    var $name = $('.facility-link');
    var $city = $('.facility-address');
    var $price = $('.facility-price');
    var $kind = $('.facility-kind'); //przechwytują tekst w tagach obiektów sportowych

    var $table = $('.facility-details-table');

    var $search_name = $('.search-name');
    var $search_city = $('.search-city');
    var $search_price_from = $('.search-price-from');
    var $search_price_to= $('.search-price-to');
    var $search_kind = $('.search-kind').find('input:checkbox:checked');

    $search_name.keyup(function(){
        var valThis = $(this).val();
        $name.each(function(){
            var text = $(this).text().toLowerCase();
            var element = $(this).parent().parent().parent().parent();
            (text.indexOf(valThis.toLowerCase()) > -1) ? element.show() : element.hide();
        });
    });

    $search_city.keyup(function(){
        var valThis = $(this).val();
        $city.each(function(){
            var text = $(this).text().toLowerCase();
            var element = $(this).parent().parent().parent().parent();
            (text.indexOf(valThis.toLowerCase()) > -1) ? element.show() : element.hide();
        });
    });


//    console.log($name.text());
//    console.log($city.text());
//    console.log($price.text());
//    console.log($kind.text());
//
//    console.log($search_name.html());
//    console.log($search_city.text());
//    console.log($search_price_from.text());
//    console.log($search_price_to.text());
//    console.log($search_kind.text());
});