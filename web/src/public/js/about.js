$(document).ready(function() {  
  $("#about").on("click", function() {
    console.log("about");
  });

  $("#toggleButton").on("click", function() {
    document.getElementById("sidebar").classList.toggle('active');
  });

  $("#aboutHeader").on("click", function() {
    if($("#sidebar").hasClass("active")) {
      console.log("responsivness measure");
    }
    else {
      window.location = "/";
    }
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
});