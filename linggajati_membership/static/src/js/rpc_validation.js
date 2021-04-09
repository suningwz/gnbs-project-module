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