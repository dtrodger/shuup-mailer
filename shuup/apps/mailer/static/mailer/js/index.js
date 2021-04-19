$(document).ready(function(){
    $("table tr").hover(function(){
            $("table *").css("background-color", ""); // remove background color from everything (un-hover)
        hoveretr = this;
    $("td:contains(.)").each(function(){

    function processchildrow(theparentrow) {
         parenttbl = $(theparentrow).parents("table");
         found = 0; // find state machine marker
         markrows = new Array();
         parenttbl.find("tr").each(function(){
             var foundrow = this;
             if(found == 0 && foundrow == theparentrow) found = 1;
             if(found == 1 && $(foundrow).is(":contains(Orders)")) {
                 orderscll= $(foundrow).find("td").eq(2);
                 numorders=+orderscll.text().split(" ")[1]; //use + for faster integer
                 if(numorders>3) markrows[markrows.length]=foundrow;//put in array for marking later
                 return
             }
             if(found == 1 && foundrow != theparentrow  &&  $(foundrow).find("td:first").text().length) // has company name in first cell
                 found = 2;
         });
         for(key in markrows) {
             row=markrows[key]
             $(row).find("td").css("background-color", "yellow");
         }
         return markrows
    }

        price = $(this).text();
        trueprice = "";
        if (price.indexOf(".", price.length - ".".length) === -1)
        {
            trueprice = price;
        }

        if (trueprice)
        {
            if (parseInt(trueprice) > 50000)
            {
                finalprice = parseInt(trueprice);
                firstsib = $(this).siblings(":first");
                therow = $(firstsib).parents("tr");

                $(therow).find("td").each(function(elem){
                    elem = $(this);

                    if(therow[0] !== hoveretr) return; // === better than ==

                    if($(elem).css("background-color"))
                        $(elem).css("background-color", ""); // remove background color

                    $(elem).css("background-color", 'green');
                    processchildrow(therow[0]);
                });
            }
            else
            {
                finalprice = parseInt(trueprice);
                firstsib = $(this).siblings(":first");
                therow = $(firstsib).parents("tr");

                $(therow).find("td").each(function(elem){
                    elem = $(this);
                    if(therow[0] !== hoveretr) return; // === better than ==

                    if($(elem).css("background-color"))
                        $(elem).css("background-color", ""); // remove background color

                    $(elem).css("background-color", 'orange');
                });
            }
        }
        });
    });
});