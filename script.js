$(document).ready(function() {
    $('#turnOnBtnR1').on('click', function(e){
        $.ajax({
            url: '/led?status=on&led=ledrelay1',
            method: 'GET',
            success: function(result) {
                console.log(result);
         }
        });
        e.preventDefault();
    });
    $('#turnOnBtnR2').on('click', function(e){
        $.ajax({
            url: '/led?status=on&led=ledrelay2',
            method: 'GET',
            success: function(result) {
                console.log(result);
         }
        });
        e.preventDefault();
    });
    $('#turnOffBtnR1').on('click', function(e){
        $.ajax({
            url: '/led?status=off&led=ledrelay1',
            method: 'GET',
            success: function(result) {
                console.log(result);
         }
        });
        e.preventDefault();
    });
    $('#turnOffBtnR2').on('click', function(e){
        $.ajax({
            url: '/led?status=off&led=ledrelay2',
            method: 'GET',
            success: function(result) {
                console.log(result);
         }
        });
        e.preventDefault();
    });
});



