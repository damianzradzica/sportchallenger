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
    var $price_searcher = $('.price-searcher');

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
            var element = $(this).parent().parent();
            (valThis.toLowerCase().includes(text) == true) ? element.show() : element.hide();
        });
    });

    $price_searcher.keyup(function(){
        var valFrom = parseInt($search_price_from.val(), 10);
        var valTo = parseInt($search_price_to.val(), 10);
        $price.each(function(){
            var text = parseInt($(this).text().match(/\d+/)[0], 10);
            var external = parseInt($search_price_to.val(), 10);
            console.log(valFrom);
            console.log(valTo);
            console.log(text);
            var element = $(this).parent().parent();
            if ($.isNumeric(valFrom) == false && $.isNumeric(valTo) == true) {
                (text<=valTo) ? element.show() : element.hide();
            }
            else if ($.isNumeric(valFrom) == true && $.isNumeric(valTo) == false) {
                (text>=valFrom) ? element.show() : element.hide();
            }
            else if ($.isNumeric(valFrom) == true && $.isNumeric(valTo) == true) {
                (valTo>=text && text>=valFrom) ? element.show() : element.hide();
            }
            else {
                (1>=0) ? element.show() : element.hide();
            };
        });
    });

//    $search_price_to.keyup(function(){
//        var valThis = parseInt($(this).val(), 10);
//        $price.each(function(){
//            var text = parseInt($(this).text().match(/\d+/)[0], 10);
//            var external = parseInt($search_price_from.val(), 10);
//            if ($.isNumeric(external) == false) {
//                external = -1;
//            };
//            console.log(valThis);
//            console.log(text);
//            var element = $(this).parent().parent();
//            ($.isNumeric(valThis) == false || text<=valThis) ? element.show() : element.hide();
//        });
//    });

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