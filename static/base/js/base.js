function searchUser(url) {
    if ($("#input-search").val().length>2){
        $.ajax({
            url:  url+"search/"+$("#input-search").val(),
            type:  'get',
            dataType:  'text/json',
            complete: function  (data) {
                if (data.status==200){
                    users = JSON.parse(data.responseText).users_found;
                    var x = "<ul class='list-users-found'>";
                    for (var i = 0; i <= users.length - 1; i++) {
                        x+="<li><a href='"+users[i].url+"'>"+users[i].username+"</a></li><hr>";
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



////validar imagen subida a formulario
$(document).on('change','input[type="file"]',function(){
    // this.files[0].size recupera el tamaño del archivo
    // alert(this.files[0].size);
    if (this.files[0]!=undefined){
        var fileName = this.files[0].name;
        var fileSize = this.files[0].size;

        if(fileSize > 5000000){
            $('#modal-alert').modal({"show":true});
            $('#modal-alert .modal-title').text("Imágen inválida")
            $('#modal-alert .modal-body').text("La imagen excede el tamaño permitido. El tamaño máximo es de 5.0MB. Por favor seleccione otra imagen.")
            this.value = '';
        }else{
        // recuperamos la extensión del archivo
        var ext = fileName.split('.').pop();
        
        // Convertimos en minúscula porque 
        // la extensión del archivo puede estar en mayúscula
        ext = ext.toLowerCase();

        // console.log(ext);
        switch (ext) {
            case 'jpg':
            case 'jpeg':
            case 'png': break;
            default:
            $('#modal-alert').modal({"show":true});    
            $('#modal-alert .modal-title').text("Archivo inválido")
            $('#modal-alert .modal-body').text("El archivo subido no corresponde a un formato permitido. Los formatos permitidos son .jpg, .jpeg, .png. Por favor seleccione otra imagen.")
                this.value = ''; // reset del valor
            }
        }
    }else{
        $('#modal-alert').modal({"show": true});    
    }
});