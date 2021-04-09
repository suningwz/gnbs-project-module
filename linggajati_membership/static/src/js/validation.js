// function validateForm() {
    
//     var x = document.forms["partner_form"]["name"].value;
//     var y = document.forms["partner_form"].value;
//     var cek = ""
//     console.log('isi x :', x)
//     console.log('isi y :', y)

//     odoo.define('linggajati_membership.validation', function (require) { 
//         let rpc = require('web.rpc')    
//         rpc.query({
//             model: 'res.partner',
//             method: 'get_all_data',
//             args: [],
//             }).then(function(res)
//                 {   
//                     console.log('res :', res);
//                     console.log('res email', res[0]);
//                     email = res[0];
//                     console.log('email :',email);
//                     // return 'ini return', email
//                     if (x == email) {
//                         cek = "False"
//                         alert("Name must be filled out");
//                         throw new Error("Manual Abort Script"); 
//                     }
//                 }); 
//         if (cek == "False") {
//             return false
//         }
//     });
//     if (cek == "False") {
//         return false
//     }
// }

// odoo.define('linggajati_membership.validation', function (require) { 

// let rpc = require('web.rpc');
// var email = "";
// console.log('Hello Abu Abi');
// console.log(rpc);
// console.log(AbstractField);
// console.log('isinya x',x);

// rpc.query({
    //     model: 'res.partner',
    //     method: 'get_all_data',
    //     args: [],
    //     }).then(function(res)
    //         {   
        //             console.log('res :', res);
        //             console.log('res email', res[0]);
        //             email = res[0];
        //             console.log('email :',email);
        //             // return 'ini return', email
        //         }); 
        
        // console.log(`Ini res_partner : ${res_partner}`);
// });

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
