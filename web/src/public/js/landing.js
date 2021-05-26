$(document).ready(function() {  
  $("#toggleButton").on("click", function() {
    document.getElementById("sidebar").classList.toggle('active');
  });
  
  $("#name").on("click", function() {
    window.location = "/";
  });
  
  $("#home").on("click", function() {
    window.location = "/";
  });
  
  $("#welcome").on("click", function() {
    window.location = "/welcome";
  });
  
  $("#about").on("click", function() {
    window.location = "/about";
  });
  
  $("#cv").on("click", function() {
    window.location = "/cv";
  });
  
  $("#avatar").on("click", function() {
    window.location = "/avatar";
  });
  
  $("#personal").on("click", function() {
    window.location = "/personal";
  });
  
  $("#education").on("click", function() {
    window.location = "/education";
  });
  
  $("#project").on("click", function() {
    window.location = "/project";
  });
  
  $("#link1").on("click", function() {
    var $url = $('#link1').html();
    window.location.href = $url;
  });
  
  $("#link2").on("click", function() {
    var $url = $('#link2').html();
    // window.location = $url;
    console.log($url);
  });
  
  $("#link3").on("click", function() {
    var $url = $('#link3').html();
    // window.location = $url;
    console.log($url);
  });

  var numPanels = $('.panel').length;

  // if a panel is open, lower its z-idx
  // otherwise, set zIdx back to original
  function checkZ($aPanel) {
    if ( $aPanel.hasClass('open') ) {
      $aPanel.css('z-index','1');
    } else {
      // set z-index back to original stored in data
      zIdx = $aPanel.data('zIdx');
      $aPanel.css( 'z-index', zIdx );
    }
  }

  // loop through all panels and reverse sort via zIdx
  for (i=0; i<(numPanels); i++  ) {
    var zIdx =  numPanels-i;
    $('.panel').eq(i).css('z-index',zIdx).data('zIdx',zIdx);
  }

  // when clicking the front panel add class 'open' to panel
  // if clicking bacl panel, remove 'open' from panel
  $('.panel').on('click', '.front, .back', function() {
    $(this).parent('.panel').toggleClass('open');
    checkZ($(this).parent('.panel'));
  });
});