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
    var $search_kind = $('.kind-check');

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
            var element = $(this).parent().parent();
            (text.indexOf(valThis.toLowerCase()) > -1) ? element.show() : element.hide();
        });
    });



    $search_kind.on('click', function(){
        var selected = '';
        $('.search-kind input:checked').each(function() {
            selected += $(this).val();
        });
        var valThis = selected.replace(/\s+/g, '');
        $kind.each(function(){
            var text = $(this).text().toLowerCase().replace('rodzaj obiektu:','').replace(/\s+/g, '');
            console.log(valThis);
            console.log(text);
            var element = $(this).parent().parent();
            (valThis.toLowerCase().includes(text) == true) ? element.show() : element.hide();
        });
    });


//    var check_elements = [];
//    check_elements.push($('.kind-check'));
//    for(i=0; i<check_elements.length; i++) {
//        if (check_elements[i].is(':checked')) {
//            console.log(check_elements[i].text());
//        }
//    };

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