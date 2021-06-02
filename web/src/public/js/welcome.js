$( document ).ready(function() {
  $("#toggleButton").on("click", function() {
    document.getElementById("sidebar").classList.toggle('active');
  });

  $.getJSON("/get_users", function(data, status) {
    if(status == "success") {
      $.each(data, function(index, value) {
        $("#guests").find('tbody')
        .append($("<tr>")
                .append($("<td>")
                        .text(value[0])
                       )
                .append($("<td>")
                        .text(value[1])
                       )
                .append($("<td>")
                        .text(value[2])
                       )
                .append($("<td>")
                        .text(value[3])
                       )
               );
      });
    }
    else {
      alert("There was a problem!");
    }
  });


  $('form').submit( function () {
    console.log( "submit" );
    var valid = true;
    
    $('input').each(function() {
      if(!$(this).val()){
        valid = false;
      }
    });

    if(valid) {
      var formdata = $(this).serialize();

      $.ajax({
          type: "POST",
          url: "/add_user",
          data: formdata
       });

      $("#guests").find('tbody')
        .append($("<tr>")
                .append($("<td>")
                        .text($("#fname").val())
                       )
                .append($("<td>")
                        .text($("#lname").val())
                       )
                .append($("<td>")
                        .text($("#email").val())
                       )
                .append($("<td>")
                        .text($("#comment").val())
                       )
               );

      alert("Thank you for your entry");
    }
    else {
      alert('Some fields are empty!');
    }

    $(this).closest('form').find("input[type=text]").val("");

    return false;
  }); 

  $("#name").on("click", function() {
    if($("#sidebar").hasClass("active")) {
      console.log("Already active");
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