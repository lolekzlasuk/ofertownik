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

            "title":$(this).parent().find('.product_id').val(),
            "pk": pk,
            // "csrfmiddlewaretoken": csrftoken,
            // "action": 'post'
        }),

        success:(json) => {
          console.log('yaaay');


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


                    },
                    error : function(xhr,errmsg,err) {
                    console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                }
                });
               });


               $( document ).ready(function(){
               $('.card--big').hide();
               $('.card').show();
                    $('.tabela').hide();
                    $('.fa-th-large').css("border-bottom","2px solid black");
               });

                  $(document).on('click','.more',function (e) {
                     var pk = $(this).attr("data-id");
                     $(this).parents('.card').hide();
                     $(".big_"+pk).show();
                     document.getElementById("big_"+pk).scrollIntoView();
                  });

                  $(document).on('click','.aless',function (d) {
                     var pk = $(this).attr("data-id");
                   document.getElementById('card__'+pk).style.display = "inline-block";
                   document.getElementById('big_'+pk).style.display = "none";
                  });

                  $(document).on('click','.moret',function (e) {
                     var pk = $(this).attr("data-id");
                     $(this).parents('tr').hide();
                     $(".big_"+pk).show();

                     document.getElementById("big_"+pk).scrollIntoView();
                  });

                  $(document).on('click','.tless',function (f) {
                     var pk = $(this).attr("data-id");
                   document.getElementById(pk).style.display = "table-row";
                   document.getElementById('big_table_'+pk).style.display = "none";

                  });
                  $(document).on('click','#chcards',function () {
                    $('.cards').show();
                    $('.tabela').hide();
                    $('.card--big').hide();
               $('.fa-th-large').css("border-bottom","2px solid black");
               $('.fa-th-list').css("border-bottom","none");
                  });
                  $(document).on('click','#chtable',function () {
                    $('.cards').hide();
                    $('.tabela').show();
               $('.card--big').hide();
               $('.fa-th-large').css("border-bottom","none");
               $('.fa-th-list').css("border-bottom","2px solid black");
                  });
