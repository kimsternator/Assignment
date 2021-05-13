$( document ).ready(function() {
  $( ".guestInfo form #submit" ).on( "click", function() {
    console.log( "submit" );
    var valid = true;
    
    $('input').each(function() {
      if(!$(this).val()){
        valid = false;
      }
    });

    if(valid) {
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
    }
    else {
      alert('Some fields are empty!');
    }

    $(this).closest('form').find("input[type=text]").val("");
  });
});