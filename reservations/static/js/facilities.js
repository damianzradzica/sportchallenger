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


    $search_name.on('change', function(event) {
        $name.each(function() {
            if ($search_name.text().indexOf($(this)) == -1) {
                $(this).parent().parent().parent().parent().toggleClass('hidden');
        }
        });

    });

    console.log($name.text());
    console.log($city.text());
    console.log($price.text());
    console.log($kind.text());

    console.log($search_name.text());
    console.log($search_city.text());
    console.log($search_price_from.text());
    console.log($search_price_to.text());
    console.log($search_kind.text());
});