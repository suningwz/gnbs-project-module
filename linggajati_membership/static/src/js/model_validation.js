let global_rpc;
let global_email;
let global_email_array = [];

odoo.define('linggajati_membership.model_validation', function (require) {
    "use strict" ;
    console.log('Hello Abu Abdi')

    global_rpc = require('web.rpc');
    console.log(global_rpc)
    // console.log('email di luar query sebelum query:',global_email);
    
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

                //  Hanya untuk cek data
                console.log('res :', res);
                console.log('res email', res[0]);
                global_email = res[0];
                console.log('email di dalam query :',global_email);
                // return 'ini return', email
            }); 

    // console.log('email di luar query setelah query:',global_email);
});

function buttonClick(){
    console.log('Success Click Button')
    console.log(global_rpc)
    console.log('email di button click:',global_email);
    console.log('global_email_array :',global_email_array)
    console.log('Length :', global_email_array.length)
    console.log('Index terakhir :', global_email_array[global_email_array.length - 1])
    console.log('Index terakhir :', global_email_array[1])
};

function validateForm() {
    var name = document.forms["partner_form"]["name"].value;
    console.log('name :', name)
    console.log('global_email_array :',global_email_array)

    i = 0
    if (global_email_array[i] === name) {
        console.log('global_email_array dalam else',i,':',global_email_array[i]);
        console.log('name',i,':',name);
        alert("Name sudah terdaftar");
        return false;
    }else {
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
            if (global_email_array[global_email_array.length - 1] !== name) {
                ValidateDOB();
                return false;
            }
        };
    }

    // var dateString = document.getElementById("datepicker").value;
    // console.log("dateString :", dateString);
    // var regex = /((0[1-9]|1[0-2])\/((0|1)[0-9]|2[0-9]|3[0-1])\/((19|20)\d\d))$/;

    // //Check whether valid dd/MM/yyyy Date Format.
    // if (regex.test(dateString)) {
    //     console.log("regex.test(dateString :", regex.test(dateString));
    //     var parts = dateString.split("/");
    //     // var parts = dateString.split("-");
    //     var dtDOB = new Date(parts[1] + "/" + parts[0] + "/" + parts[2]);
    //     console.log("dtDOB :", dtDOB)
    //     //Get date of today, ex result: Tue Apr 13 2021 07:38:04 GMT+0700 (Western Indonesia Time)
    //     var dtCurrent = new Date();
    //     // lblError.innerHTML = "Umur dari siswa harus lebih dari 10 tahun!"
    //     if (dtCurrent.getFullYear() - dtDOB.getFullYear() < 10) {
    //         alert("Umur dari siswa harus lebih dari 10 tahun!");
    //         return false;
    //     }

    //     if (dtCurrent.getFullYear() - dtDOB.getFullYear() == 10) {

    //         //CD: 11/06/2018 and DB: 15/07/2000. Will turned 18 on 15/07/2018.
    //         if (dtCurrent.getMonth() < dtDOB.getMonth()) {
    //             alert("Umur dari siswa harus lebih dari 10 tahun!");
    //             return false;
    //         }
    //         if (dtCurrent.getMonth() == dtDOB.getMonth()) {
    //             //CD: 11/06/2018 and DB: 15/06/2000. Will turned 18 on 15/06/2018.
    //             if (dtCurrent.getDate() < dtDOB.getDate()) {
    //                 alert("Umur dari siswa harus lebih dari 10 tahun!");
    //                 return false;
    //             }
    //         }
    //     }
    //     lblError.innerHTML = "";
    //     return true;
    // } else {
    //     // lblError.innerHTML = "Enter date in dd/MM/yyyy format ONLY."
    //     return false;
    // }
};

function ValidateDOB() {
    // var lblError = document.getElementById("lblError");

    //Get the date from the TextBox.
    var dateString = document.getElementById("datepicker").value;
    console.log("dateString :", dateString);
    var regex = /((0[1-9]|1[0-2])\/((0|1)[0-9]|2[0-9]|3[0-1])\/((19|20)\d\d))$/;

    //Check whether valid dd/MM/yyyy Date Format.
    if (regex.test(dateString)) {
        console.log("regex.test(dateString :", regex.test(dateString));
        var parts = dateString.split("/");
        // var parts = dateString.split("-");
        var dtDOB = new Date(parts[1] + "/" + parts[0] + "/" + parts[2]);
        console.log("dtDOB :", dtDOB)
        //Get date of today, ex result: Tue Apr 13 2021 07:38:04 GMT+0700 (Western Indonesia Time)
        var dtCurrent = new Date();
        // lblError.innerHTML = "Umur dari siswa harus lebih dari 10 tahun!"
        if (dtCurrent.getFullYear() - dtDOB.getFullYear() < 5) {
            alert("Umur dari siswa harus lebih dari 5 tahun!");
            return false;
        }

        if (dtCurrent.getFullYear() - dtDOB.getFullYear() == 5) {

            //CD: 11/06/2018 and DB: 15/07/2000. Will turned 18 on 15/07/2018.
            if (dtCurrent.getMonth() < dtDOB.getMonth()) {
                alert("Umur dari siswa harus lebih dari 5 tahun!");
                return false;
            }
            if (dtCurrent.getMonth() == dtDOB.getMonth()) {
                //CD: 11/06/2018 and DB: 15/06/2000. Will turned 18 on 15/06/2018.
                if (dtCurrent.getDate() < dtDOB.getDate()) {
                    alert("Umur dari siswa harus lebih dari 5 tahun!");
                    return false;
                }
            }
        }
        lblError.innerHTML = "";
        return true;
    } else {
        // lblError.innerHTML = "Enter date in dd/MM/yyyy format ONLY."
        return false;
    }
}

$(document).ready(function(){
    $('.datepicker').datepicker({
        changeMonth: true,
        changeYear: true,
        showButtonPanel: true,
        selectOtherMonths: true,
        autoclose: true,
        todayHighlight: true,
        yearRange: "-20:+0"
    })
})
