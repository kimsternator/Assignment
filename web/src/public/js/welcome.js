$( document ).ready(function() {
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
});