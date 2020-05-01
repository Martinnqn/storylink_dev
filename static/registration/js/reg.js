$(document).ready(function() {
    var params = getParameters();
    for (var i = params.length - 1; i >= 0; i--) {
        if (params[i][0]=='used' && params[i][1]=='True'){
        	$('.msg').html('<p>El e-mail asociado a esta cuenta ya está en uso, por favor ingrese un nuevo e-mail.</p>')
        }
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
  if (prevScrollpos + 120 > currentScrollPos) {
    document.getElementById("header-base").style.top = "0";
  } else {
    document.getElementById("header-base").style.top = "-190px";
  }
    prevScrollpos = currentScrollPos;
}


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
});