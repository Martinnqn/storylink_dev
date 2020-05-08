$(document).ready(function() {
  var is_used = false;
  var params = getParameters();
  for (var i = params.length - 1; i >= 0; i--) {
    if (params[i][0]=='used' && params[i][1]=='True'){
      is_used = true;
      $('.msg').html('<p>Lo sentimos, el e-mail asociado a esta cuenta ya se encuentra en uso. </p><p>Por favor, pruebe <a href="/">iniciar sesión con otra cuenta.</a> </p>')
    }
  }
  if (!is_used){
    $('.msg').html('<p>Lo sentimos, requerimos un email para completar el proceso de registro.'+
      '<p>Utilizamos el e-mail para verificar la identidad de nuestros usuarios, y para ayudarlos '+
      'ante cualquier inconveniente con la plataforma, por ejemplo, para brindarles servicio cuando '+
      'olvidan sus credenciales de inicio de sesión.</p>')
  }
});

$(document).ready(function() {
  console.log("entra")
  if (success=='True'){
    $('#modal-alert').modal({"show":true});
    $('#modal-alert .modal-title').text("¡Cuenta creada con éxito!")
    $('#modal-alert .modal-body').html("<h5>Gracias por crear una cuenta en Storylink</h5>"+
      "<p>Para completar el registro, por favor ingrese a su cuenta de correo electrónico y haga click en el enlace"+
      " que se le ha enviado para activar su cuenta.</p>"+
      "<p>Si <strong>no puede</strong> encontrar el correo electrónico, por favor revise su correo no deseado.</p>")
  }else if(email_verified=='True'){
    $('#modal-alert').modal({"show":true});
    $('#modal-alert .modal-title').text("¡Email verificado con éxito!")
    $('#modal-alert .modal-body').html("<h5>Gracias por verificar su email</h5>"+
      "<p>El proceso de creación de cuenta ha terminado.</p>"+
      "<p>Antes de poder iniciar sesión, debe agregar informacion a su perfil. No es obligatorio llenar los campos!</p>")
  }else if (email_verified=='False'){
    $('#modal-alert').modal({"show":true});
    $('#modal-alert .modal-title').text(":(")
    $('#modal-alert .modal-body').html("<h5>El link de verificación de email es inválido.</h5>")
  }
});

/*funcion para obtener un arreglo con los parametros de la url*/
function getParameters() {
  var res=[];
  if (location.search){
    location.search.substr(1).split("&").forEach(function(param) {
        var s = param.split("="), //separamos llave/valor
        ll = s[0],
        v =  decodeURIComponent(s[1]);
        res.push([ll,v]); //si es nula, quiere decir que no tiene valor, solo textual
      });
  }
  return res;
}


/* When the user scrolls down, hide the navbar. When the user scrolls up, show the navbar */
var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("header-base").style.top = "0";
  } else {
    document.getElementById("header-base").style.top = "-190px";
  }
  prevScrollpos = currentScrollPos;
}

/*
$(document).ready(function(){
  // Add smooth scrolling to all links
  $("a").on('click', function(event) {

    // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
      // Prevent default anchor click behavior
      event.preventDefault();

      // Store hash
      var hash = this.hash;

      // Using jQuery's animate() method to add smooth page scroll
      // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 800, function(){

        // Add hash (#) to URL when done scrolling (default click behavior)
        window.location.hash = hash;
      });
    } // End if
  });
});*/

function animateScroll(target) {
    /*console.log($('#theater-main').scrollTop())
    console.log($('#theater-main').offset().top)
    console.log($(target).scrollTop())
    console.log($(target).offset().top)
    console.log("resss")
    console.log($('#theater-main').scrollTop()+($(target).offset().top-window.pageYOffset))
    alert(window.pageYOffset-$(target).offset().top)
    alert($(target).offset().top)*/
    //el scrollTop necesita restarle el pageYoffset porque nose pero funciona.
    console.log($(target).offset().top)
    console.log($('body').scrollTop())
    $('html, body').animate({
      scrollTop: $('body').scrollTop()+$(target).offset().top,
    }, 800);

  }