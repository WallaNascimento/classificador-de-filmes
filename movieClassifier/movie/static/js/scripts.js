function showMessage(){
    var msg = document.getElementById('message');
  msg.textContent = 'Faça login!';
  }

  
  function addEvaluation() {
    $idMovie=document.getElementById('idMovie').value
              $cla=document.getElementById('cla').value
              $fcomment=document.getElementById('fcomment').value
          
              $.ajax({
                      type: 'POST',
             url: '/evaluation/',
                         contentType: 'application/json',
                       
                       headers: {
               "X-CSRFToken": '{{ csrf_token }}',
             },
            data:{
          idMovie:$idMovie,
          cla:$cla,
          fcomment:$fcomment,     
            },
  
              'dataType': 'json',
            success: function (data) {
                // location.reload();           
                
            },
            error: function (error) {
              
              console.log(`Error ${error}`);
            }
          });
        }

        function updateEvaluation(id) {
            $.ajax({
      'type': 'POST',
      'url': '/getEvaluationInfo/' + id + '/',
      'contentType': 'application/json',
      headers: {
        "X-CSRFToken": '{{ csrf_token }}',
      },
      'data': {
      },
      'dataType': 'json',
      success: function (data) {
        idMovieOfMovie = data.idMovie;
        fclaOfMovie = data.fcla;
        commentOfMovie = data.comment;
         $('#modalExemploUpdate').modal();
        document.getElementById("idMovie").value = idMovieOfMovie
        document.getElementById("fcla").value = fclaOfMovie
        document.getElementById("comment").value = commentOfMovie
        $('#formUpdate').attr('action', 'http://127.0.0.1:8000/updateEvaluation/' + id + '/');
      },
      error: function (error) {
        console.log(`Error ${error}`);
      }
    });
  }

  function userFollower(id) {
          
    $.ajax({
                type: 'POST',
       url: '/follow/' +id+'/',
                  contentType: 'application/json',
                 
                 headers: {
         "X-CSRFToken": '{{ csrf_token }}',
       },
      data:{ 
      },

      'dataType': 'json',
      success: function (data) {
        location.reload();           
                  },
      error: function (error) {
        
        console.log(`Error ${error}`);
      }
    });
  }

  function like(id) {
          
    $.ajax({
                type: 'POST',
       url: '/like/' +id+'/',
                  contentType: 'application/json',
                 
                 headers: {
         "X-CSRFToken": '{{ csrf_token }}',
       },
      data:{ 
      },

      'dataType': 'json',
      success: function (data) {
        location.reload();           
                  },
      error: function (error) {
        
        console.log(`Error ${error}`);
      }
    });
  }

  function dislike(id) {
          
    $.ajax({
                type: 'POST',
       url: '/dislike/' +id+'/',
                  contentType: 'application/json',
                 
                 headers: {
         "X-CSRFToken": '{{ csrf_token }}',
       },
      data:{ 
      },

      'dataType': 'json',
      success: function (data) {
        location.reload();           
                 },
      error: function (error) {
        
        console.log(`Error ${error}`);
      }
    });
  }

function addMoviePlaylist(id) {
          
    $.ajax({
                type: 'POST',
       url: '/addMoviePlaylist/' +id+'/',
                  contentType: 'application/json',
                 
                 headers: {
         "X-CSRFToken": '{{ csrf_token }}',
       },
      data:{ 
      },

      'dataType': 'json',
      success: function (data) {
        location.reload();           
                  },
      error: function (error) {
        
        console.log(`Error ${error}`);
      }
    });
  }

  function addMovieWatched(id) {
          
    $.ajax({
                type: 'POST',
       url: '/movieWatched/' +id+'/',
                  contentType: 'application/json',
                 
                 headers: {
         "X-CSRFToken": '{{ csrf_token }}',
       },
      data:{ 
      },

      'dataType': 'json',
      success: function (data) {
        location.reload();           
                  },
      error: function (error) {
        
        console.log(`Error ${error}`);
      }
    });
  }
