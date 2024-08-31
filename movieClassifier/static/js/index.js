function deleteMovie(id) {
  var result = confirm("Tem certeza?");
  if (result) {

    $.ajax({
      type: 'POST',
      url: '/deleteMovie/' + id + '/',
      contentType: 'application/json',

      headers: {
        "X-CSRFToken": '{{ csrf_token }}',
      },
      data: {
      },

      'dataType': 'json',
      success: function (data) {
        document.getElementById(id).remove();
      },
      error: function (error) {

        console.log(`Error ${error}`);
      }
    });
  }
}

function addMovie() {
  $('#form').on('submit', function (e) {
    e.preventDefault(); // Evita o envio padrão do formulário 
    var formData = new FormData(this);
    $.ajax({
      type: 'POST',
      url: '/addMovie/',

      headers: {
        "X-CSRFToken": '{{ csrf_token }}',
      },

      data: formData,
      contentType: false,
      processData: false,

      success: function (data) {
        location.reload();

      },
      error: function (error) {

        console.log(`Error ${error}`);
      }
    });
  });
}

function updateMovie(id) {
  $.ajax({
    'type': 'POST',
    'url': '/update/' + id + '/',
    'contentType': 'application/json',
    headers: {
      "X-CSRFToken": '{{ csrf_token }}',
    },
    'data': {
    },
    'dataType': 'json',
    success: function (data) {
      nameOfMovie = data.name;
      durationOfMovie = data.duration;
      descriptionOfMovie = data.description;
      $('#modalExemploUpdate').modal();
      document.getElementById("name").value = nameOfMovie
      document.getElementById("duration").value = durationOfMovie
      document.getElementById("description").value = descriptionOfMovie
      $('#formUpdate').attr('action', 'http://127.0.0.1:8000/updateMovie/' + id + '/');
    },
    error: function (error) {
      console.log(`Error ${error}`);
    }
  });
}
