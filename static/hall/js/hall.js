$(document).ready(function() {
  if(activated=='True'){
    $('#modal-alert').modal({"show":true});
    $('#modal-alert .modal-title').text("¡Cuenta activada con éxito!")
    $('#modal-alert .modal-body').html("<h5>Gracias por completar el proceso de registro</h5>"+
      "<p>¡Diviertete!</p>")
  }else if (activated=='False'){
    $('#modal-alert').modal({"show":true});
    $('#modal-alert .modal-title').text(":(")
    $('#modal-alert .modal-body').html("<h5>El link de activación de cuenta es inválido.</h5>")
  }
});
