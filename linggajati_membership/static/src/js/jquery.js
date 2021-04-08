odoo.define('linggajati_membership.validation', function (require) {
    "use strict";

    let rpc = require('web.rpc');
    console.log('Hello Abu');
    console.log(rpc);

    rpc.query({
        model: 'res.partner',
        method: 'get_all_data',
        args: [],
        }).then(function(res)
        {
        //    let email= res.email
           console.log('res :', res)
           console.log('res email', res[0])
           let email = res[0]
           function validateForm() {
                var x = document.forms["myForm"]["fname"].value;
                if (x == "") {
                    alert("Name must be filled out");
                    return false;
                }};
        });
});