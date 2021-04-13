$(document).ready(function(){
    // $('#date').datepicker({  
    //     format: 'dd/mm/yyyy'  
    //   });  
    // $(".button_click").click()
    $(".button_click").click(function(){
        alert("The paragraph was clicked.");
      });
    $('.datepicker').datepicker({
        // format: 'dd/mm/yyyy',
        format: 'yyyy-mm-dd',
        // startDate: '-3d',
        changeMonth: true,
        changeYear: true,
        showButtonPanel: true,
        selectOtherMonths: true,
        autoclose: true,
        todayHighlight: true,
    })
})

function ValidateDOB() {
    var lblError = document.getElementById("lblError");

    //Get the date from the TextBox.
    //In Bootstrap the value be : 2021-04-03 ( 3 April 2021)
    var dateString = document.getElementById("datepicker").value;
    console.log("dateString :", dateString);
    // 24/05/2015
    // var regex = /(((0|1)[0-9]|2[0-9]|3[0-1])\/(0[1-9]|1[0-2])\/((19|20)\d\d))$/;
    // 2015-11-24
    // var regex = /(((19|20)\d\d)\-((0|1)[0-9]|2[0-9]|3[0-1])\-(0[1-9]|1[0-2]))$/;
    // 05/24/2015
    var regex = /((0[1-9]|1[0-2])\/((0|1)[0-9]|2[0-9]|3[0-1])\/((19|20)\d\d))$/;

    //Check whether valid dd/MM/yyyy Date Format.
    if (regex.test(dateString)) {
        console.log("regex.test(dateString :", regex.test(dateString));
        var parts = dateString.split("/");
        // var parts = dateString.split("-");
        var dtDOB = new Date(parts[1] + "/" + parts[0] + "/" + parts[2]);
        // var dtDOB = new Date(parts[0] + "/" + parts[1] + "/" + parts[2]);
        console.log("dtDOB :", dtDOB)
        //Get date of today, ex result: Tue Apr 13 2021 07:38:04 GMT+0700 (Western Indonesia Time)
        var dtCurrent = new Date();
        lblError.innerHTML = "Umur dari siswa harus lebih dari 10 tahun!"
        if (dtCurrent.getFullYear() - dtDOB.getFullYear() < 10) {
            return false;
        }

        if (dtCurrent.getFullYear() - dtDOB.getFullYear() == 10) {

            //CD: 11/06/2018 and DB: 15/07/2000. Will turned 18 on 15/07/2018.
            if (dtCurrent.getMonth() < dtDOB.getMonth()) {
                return false;
            }
            if (dtCurrent.getMonth() == dtDOB.getMonth()) {
                //CD: 11/06/2018 and DB: 15/06/2000. Will turned 18 on 15/06/2018.
                if (dtCurrent.getDate() < dtDOB.getDate()) {
                    return false;
                }
            }
        }
        lblError.innerHTML = "";
        return true;
    } else {
        lblError.innerHTML = "Enter date in dd/MM/yyyy format ONLY."
        return false;
    }
}