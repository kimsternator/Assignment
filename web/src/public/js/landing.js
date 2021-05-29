$(document).ready(function() { 
  function load_class() {
    $.getJSON("/get_class", function(data, status) {
      if(status == "success") {
        var len = data["urls"].length;

        for(i = 0; i < len - len % 2; i+=2) {
          $("#flipBook").append($("<div>")
                          .addClass("panel")
                          .css("style", "z-index: 1;")
                          .append($("<div>")
                            .addClass("front")
                            .append($("<div>")
                              .addClass("content")
                              .append($("<p>")
                                .addClass("classLink")
                                .html(data["urls"][i]))
                                .append($("<div>")
                                  .addClass("box")
                                  .append($("<iframe>")
                                    .attr("src", data["urls"][i])
                                    .attr("loading", "lazy")
                                    .attr("scrolling", "no")
                                    .addClass("display")))))
                          .append($("<div>")
                            .addClass("back")
                            .append($("<div>")
                              .addClass("content")
                              .append($("<p>")
                                .addClass("classLink")
                                .html(data["urls"][i + 1]))
                                .append($("<div>")
                                  .addClass("box")
                                  .append($("<iframe>")
                                    .attr("src", data["urls"][i + 1])
                                    .attr("loading", "lazy")
                                    .attr("scrolling", "no")
                                    .addClass("display"))))));
        }

        if(len % 2 != 0) {
          $("#flipBook").append($("<div>")
                          .addClass("panel")
                          .css("style", "z-index: 1;")
                          .append($("<div>")
                            .addClass("front")
                            .append($("<div>")
                              .addClass("content")
                              .append($("<p>")
                                .addClass("classLink")
                                .html(data["urls"][len - 1]))
                                .append($("<div>")
                                  .addClass("box")
                                  .append($("<iframe>")
                                    .attr("src", data["urls"][len - 1])
                                    .attr("loading", "lazy")
                                    .attr("scrolling", "no")
                                    .addClass("display")))))
                          .append($("<div>")
                            .addClass("back")
                            .append($("<div>")
                              .addClass("content")
                                    .addClass("display"))));
        }
      }
      else {
        alert("There was a problem!");
      }

      var numPanels = $('.panel').length;
      console.log(numPanels);
      // loop through all panels and reverse sort via zIdx
      for (i=0; i<(numPanels); i++  ) {
        var zIdx =  numPanels-i;
        $('.panel').eq(i).css('z-index',zIdx).data('zIdx',zIdx);
      }

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

      // when clicking the front panel add class 'open' to panel
      // if clicking bacl panel, remove 'open' from panel
      $('#flipBook .panel').on('click', '.front, .back', function() {
        console.log(this);
        $(this).parent('.panel').toggleClass('open');
        checkZ($(this).parent('.panel'));
      });
    });
  }

  load_class();

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

  $("#flipBook").on("click", ".classLink", function() {
    var $url = $(this).html();
    window.location.href = $url;
  });
});