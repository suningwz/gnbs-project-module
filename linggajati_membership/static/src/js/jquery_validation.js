$(document).ready(function(){
    $("#submit" ).mouseenter(function() {

        odoo.define('linggajati_membership.validation', function (require) {
            // let rpc = 'AAA'
            let odoo_define = {};
            let a = "AAA";
            odoo_define.name = a
            let rpc = require('web.rpc')  
            console.log('a di atas :',a);
            console.log('rpc :',rpc);
            return a;
        });

        // let rpc_email = rpc
        // console.log('rpc', rpc)
        console.log('a di bawah :',odoo_define.name);
        var x = $("#name").val()
        if (x == 'AA') {
            alert( "Handler for .click() called." );
            return false;
        }
    });

    // var validateForm = function(){
    //     var x = $('#name').val();
    //     console.log('isi x', x)
    //     if (x == 'AA') {
    //         alert("Name must be filled out");
    //         return false;
    //     }
    // }
    
    // validateForm()

});