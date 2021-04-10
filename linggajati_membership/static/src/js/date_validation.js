// let date;

// odoo.define('linggajati_membership.date_validation', function () {

//     console.log('date :', date)
    
// });

// function buttonClick(){
//     date = document.forms["partner_form"]["date"].value;
//     console.log('Success Click Button')
//     console.log('Date :', date)
// };

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
    $("#dp3").datepicker();
    $('select').on('change', function () {
        var d = $('select option:selected').text();
        if (d == 2) {
            $("#dp3").datepicker('remove');
            $("#dp3").datepicker({
                format: "dd/mm/yyyy"
            })
        }
        else {
            $("#dp3").datepicker('remove');
            $("#dp3").datepicker({
                format: "mm/dd/yyyy"
            })
        }
    });
})

// $(".datepicker").datepicker({
//     // format: 'yyyy-mm-dd',
//     // autoclose: true,
//     // todayHighlight: true,
//     showButtonPanel: true,
//     changeMonth: true,
//     changeYear: true,
//     showOtherMonths: true,
//     selectOtherMonths: true 
// });

// $('.datepicker').datepicker({
//     format: 'mm/dd/yyyy',
//     startDate: '-3d'
// })

// $('#datepicker').datepicker('show');
    
// $(function(){
//    });