
let global_email = [];

odoo.define('linggajati_school.validation', function (require) {
    "use strict" ;
    console.log('CEK')

    let rpc = require('web.rpc');
    rpc.query({
        model: 'res.partner',
        method: 'get_all_data',
        args: [],
        }).then(function(res)
            {   
                res.forEach(data => {
                    global_email.push(data)
                });
            }); 
});

function validateForm() {
    //Get the email from the TextBox.
    var email = document.forms["student_form"]["email"].value;
    console.log("email: " + email);
    
    //Check whether email valid
    i = 0
    if (global_email[i] === email) {
        alert("Email sudah terdaftar");
        return false;
    } else {
        while (global_email[i] != email) {
            if (global_email[i] === email) {
                alert("Email sudah terdaftar");
                return false;
            };
            if (global_email[global_email.length - 1] !== email) {
                ValidateDOB();
                return false;
            };
        };
    };
};

function ValidateDOB() {

    //Get the date from the TextBox.
    var dateString = document.getElementById("datepicker").value;
    console.log("dateString :", dateString);
    var regex = /((0[1-9]|1[0-2])\/((0|1)[0-9]|2[0-9]|3[0-1])\/((19|20)\d\d))$/;

    //Check whether valid dd/MM/yyyy Date Format.
    if (regex.test(dateString)) {
        console.log("regex.test(dateString :", regex.test(dateString));
        var parts = dateString.split("/");
        var dtDOB = new Date(parts[1] + "/" + parts[0] + "/" + parts[2]);
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
        return true;
    } else {
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
