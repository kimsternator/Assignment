$( document ).ready(function() {
  $( "#link" ).on( "click", function() {
    var $url = $('#link').html();
    window.location = $url;
  });
});