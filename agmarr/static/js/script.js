$(document).ready(function(){
  $.ajaxSetup({
       beforeSend: function(xhr, settings) {
           function getCookie(name) {
               var cookieValue = null;
               if (document.cookie && document.cookie != '') {
                   var cookies = document.cookie.split(';');
                   for (var i = 0; i < cookies.length; i++) {
                       var cookie = jQuery.trim(cookies[i]);
                       // Does this cookie string begin with the name we want?
                       if (cookie.substring(0, name.length + 1) == (name + '=')) {
                           cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                           break;
                       }
                   }
               }
               return cookieValue;
           }
           if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
               // Only send the token to relative URLs i.e. locally.
               xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
           }
       }
  });

});

$(document).on('click','.product_submit',function (e) {
  var csrftoken = $("input[name=csrfmiddlewaretoken]").val();
  e.preventDefault();
  var pk = $(this).attr("data-id");
  var urlss = $(this).attr("data-href");
  console.log($(this).parent().find('.product_id').val())
    // console.log($(this).find("input[name='type"+i+"']:checked").val());
    $.ajax({
        type:'POST',
        url: urlss,
        data:JSON.stringify({
            "choice":$(this).parent().find('.catalogue').val(),
            "title":$(this).parent().find('.product_id').val(),
            "pk": pk,
            // "csrfmiddlewaretoken": csrftoken,
            // "action": 'post'
        }),

        success:(json) => {
          console.log('yaaay');
          location.reload();


        },
        error : function(xhr,errmsg,err) {
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    }
    });
   });
   $(document).on('click','.contact-form',function (e) {
     var csrftoken = $("input[name=csrfmiddlewaretoken]").val();
     e.preventDefault();

        var urlss = $(this).attr("data-href");
    var sur = document.getElementById("mailsurname").value;
    console.log(sur)
       // console.log($(this).find("input[name='type"+i+"']:checked").val());
       $.ajax({
           type:'POST',
           url: urlss,
           data:JSON.stringify({

               "name":document.getElementById("mailname").value,
              "surname":document.getElementById("mailsurname").value,
              "subject":document.getElementById("mailsubject").value,
              "mailfrom":document.getElementById("mailsender").value,
              "telephone":document.getElementById("mailtelephone").value,
              "message":document.getElementById("mailmessage").value,

           }),

           success:(json) => {
             $('#myform')[0].reset();
               alert("Wiadomość została wysłana!");


           },
           error : function(xhr,errmsg,err) {
           console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
       }
       });
      });












   $(document).on('click','.deleteproduct',function (e) {
     var csrftoken = $("input[name=csrfmiddlewaretoken]").val();
     e.preventDefault();
     var pk = $(this).attr("data-id");
     var urlss = $(this).attr("data-href");

       // console.log($(this).find("input[name='type"+i+"']:checked").val());
       $.ajax({
           type:'POST',
           url: urlss,
           data:JSON.stringify({

               "pk": pk,
               // "csrfmiddlewaretoken": csrftoken,
               // "action": 'post'
           }),

           success:(json) => {
             console.log('yaaay');
location.reload();

           },
           error : function(xhr,errmsg,err) {
           console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
       }
       });
      });

      $(document).on('click','.editproduct',function (e) {
        var csrftoken = $("input[name=csrfmiddlewaretoken]").val();
        e.preventDefault();
        var pk = $(this).attr("data-id");
        var urlss = $(this).attr("data-href");
        var el = $(this).parents(".addproduct");

          // console.log($(this).find("input[name='type"+i+"']:checked").val());
          $.ajax({
              type:'POST',
              url: urlss,
              data:JSON.stringify({
                  "title": el.find(".title").val(),
                  "price": el.find(".price").val(),
                  "material": el.find(".material").val(),
                  "description": el.find(".description").val(),
                  "size": el.find(".size").val(),
                  // "title":$(this).parent().find('.product_id').val(),
                  "pk": pk,
                  // // "csrfmiddlewaretoken": csrftoken,
                  // // "action": 'post'
              }),

              success:(json) => {
                console.log('yaaay');
location.reload();

              },
              error : function(xhr,errmsg,err) {
              console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
          }
          });
         });


            $(document).on('click','.image_submit',function (e) {
              var csrftoken = $("input[name=csrfmiddlewaretoken]").val();
              e.preventDefault();
              var pk = $(this).attr("data-id");
              var urlss = $(this).attr("data-href");
              var img = $(this).parent().find(".image_adress").val()
                // console.log($(this).find("input[name='type"+i+"']:checked").val());
                $.ajax({
                    type:'POST',
                    url: urlss,
                    data:JSON.stringify({

                        "pk": pk,
                        "adress": img
                        // "csrfmiddlewaretoken": csrftoken,
                        // "action": 'post'
                    }),

                    success:(json) => {
                      console.log('yaaay');
location.reload();

                    },
                    error : function(xhr,errmsg,err) {
                    console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                }
                });
               });
