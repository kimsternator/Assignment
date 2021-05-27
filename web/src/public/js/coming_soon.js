$( document ).ready(function() {
  var theDate = new Date(2021, 4, 31);
  var day = 86400;
  var hour = 3600;
  var minute = 60;

  $(function count() {
    var note = $('#note'),
        ts = new Date(new Date($.now()));

    var seconds = Math.round((theDate.getTime() - ts.getTime()) / 1000);
    var days, hours, minutes;
    if(seconds <= 0) {
      days = Math.floor(seconds / day);
      seconds = seconds - days * day;
      hours = Math.floor(seconds / hour);
      seconds = seconds - hours * hour;
      minutes = Math.floor(seconds / minute);
      seconds = seconds - minutes * minute;
    }
    else {
      days = 0;
      hours = 0;
      seconds = 0;
    }

    $("#countdown").text(days + "d " + hours + "h " + minutes + "m " + seconds + "s");

   setInterval(count, 1000);
  });
});

