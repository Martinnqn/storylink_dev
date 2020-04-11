function searchUser(url) {
    if ($("#input-search").val().length>2){
        $.ajax({
            url:  url+"search/"+$("#input-search").val(),
            type:  'get',
            dataType:  'text/json',
            complete: function  (data) {
                if (data.status==200){
                    users = JSON.parse(data.responseText).users_found;
                    var x = "<ul class=''>";
                    for (var i = 0; i <= users.length - 1; i++) {
                        x+="<li><a href='"+users[i].url+"'>"+users[i].username+"</a></li>";
                    }
                    x+="</ul>";
                    $("#users-found").html(x);
                }else{
                    $("#users-found").html("");
                }
            }
        });
    }
}

/*$("#form-search").focusout(function(event){
    console.log(event)
    $("#users-found").html("");
})*/

$("body").click(function (event) {
    if (event.target.id!="users-found"){
        $("#users-found").html("");
    }
})

/*para salir del search de users*/
$('body').on('keydown', function (e) {
    if (e.which == 27) {
        $("#users-found").html("");
    }
});

/*Para gestionar las cookies*/
document.addEventListener('DOMContentLoaded', () => {

    let cookies = () => {
        //======================================================================
        // COOKIES
        //======================================================================

        //-----------------------------------------------------
        // Variables
        //-----------------------------------------------------
        let seccionCookie = document.querySelector('section.cookies');
        let cookieSi = document.querySelector('.cookies__boton--si');
        let cookieNo = document.querySelector('.cookies__boton--no');

        //-----------------------------------------------------
        // Funciones
        //-----------------------------------------------------

        /**
         * Método que oculta la sección de Cookie para siempre
         */
        function ocultarCookie() {
            // Borra la sección de cookies en el HTML
            seccionCookie.remove();
        }

        /**
         * Método que marca las cookies como aceptadas
         */
        function aceptarCookies() {
            // Oculta el HTML de cookies
            ocultarCookie()
            // Guarda que ha aceptado
            localStorage.setItem('aceptacookie', true);
            // Tu codigo a ejecutar si aceptan las cookies
            ejecutarSiAcepta();
        }

        /**
         * Método que marca las cookies como denegadas
         */
        function denegarCookies() {
            // Oculta el HTML de cookies
            ocultarCookie()
            // Guarda que ha aceptado
            localStorage.setItem('aceptacookie', false);
        }

        /**
         * Método que ejecuta tu código si aceptan las cookies
         */
        function ejecutarSiAcepta() {
            /////////////////// Tu código ////////////////
            // Google Analitics
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'UA-162832086-1');
        }

        /**
         * Método que inicia la lógica
         */
        function iniciar() {
            // Comprueba si en el pasado el usuario ha marcado una opción
            if (localStorage.getItem('aceptacookie') !== null) {
                if(localStorage.getItem('aceptacookie') === 'true') {
                    // Aceptó
                    aceptarCookies();
                } else {
                    // No aceptó
                    denegarCookies();
                }
            }
        }

        //-----------------------------------------------------
        // Eventos
        //-----------------------------------------------------
        cookieSi.addEventListener('click',aceptarCookies, false);
        cookieNo.addEventListener('click',denegarCookies, false);

        return {
            iniciar: iniciar
        }
    }

    // Activa el código. Comenta si quieres desactivarlo.
    cookies().iniciar();

});