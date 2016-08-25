$(document).ready(function() {
       $("#test").submit(function(event){
            $.ajax({
                 type:"POST",
                 url:"/edit_favorites/",
                 data: {
                        'video': $('#test').val() // from form
                        },
                 success: function(){
                     $('#message').html("<h2>Contact Form Submitted!</h2>") 
                 }
            });
            return false; //<---- move it here
       });

});