
// Date picker for forms
// Credit https://simpleisbetterthancomplex.com/tutorial/2019/01/03/how-to-use-date-picker-with-django.html
$(function () {
    $("#id_requested_date").datepicker({
      format:'dd/mm/yyyy',
    });
  });