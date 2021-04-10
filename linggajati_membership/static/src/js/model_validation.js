let global_rpc;
let global_email;
let global_email_array = [];

odoo.define('linggajati_membership.model_validation', function (require) {
    "use strict" ;
    console.log('Hello Abu Abdi')

    global_rpc = require('web.rpc');
    console.log(global_rpc)
    console.log('email di luar query sebelum query:',global_email);
    
    global_rpc.query({
        model: 'res.partner',
        method: 'get_all_data',
        args: [],
        }).then(function(res)
            {   
                res.forEach(data => {
                    // console.log(data);
                    global_email_array.push(data)
                });

                console.log('res :', res);
                console.log('res email', res[0]);
                global_email = res[0];
                console.log('email di dalam query :',global_email);
                // return 'ini return', email
            }); 

    console.log('email di luar query setelah query:',global_email);
});

function callback(){
    console.log('Hello World');
};

function buttonClick(){
    console.log('Success Click Button')
    console.log(global_rpc)
    console.log('email di button click:',global_email);
    console.log('global_email_array :',global_email_array)
};

function validateForm() {
    var name = document.forms["partner_form"]["name"].value;
    console.log('name :', name)

    // global_email_array.forEach(data => {
    //     if (name == data) {
    //         alert("Name sudah terdaftar");
    //         return false;
    //     }
    // });
    i = 0
    while (global_email_array[i] != name) {
        console.log('global_email_array',i,':',global_email_array[i]);
        if (global_email_array[i] !== name) {
            i++;
            console.log('looping :',i)
        };
        if (global_email_array[i] === name) {
            console.log('global_email_array dalam else',i,':',global_email_array[i]);
            console.log('name',i,':',name);
            alert("Name sudah terdaftar");
            return false;
        };
    };
};
