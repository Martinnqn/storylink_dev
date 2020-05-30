$('#submitBtnEdit').click(function() {
   var value = $("input[name='status']:checked"). val();
   var list = getConf($("input[name='status']")[1].disabled, value);
   $('#attributes').html(list);
   $('#attributes').append('<p>¿Confirmar cambios?</p>');
});

$('#submitBtnCreate').click(function() {
    var value = $("input[name='status']:checked"). val();
    var list = getConf($("input[name='status']")[1].disabled, value);
    $('#attributes').html(list);
    $('#attributes').append('<p>¿Crear Storylink?</p>');
});

$('#submit').click(function(){
    $('#story_form').submit();
});


function getConf(bool, value) {
   var list = ''
    //Si la opcion 1 (o 2) esta disabled, es porque ya no se pueden cambiar los permisos.
    if (!bool){
       list = '<ul>'
       if (value=='WR'){
        list+='<li>Lo usuarios podrán <strong>leer y continuar</strong> la publicación.</li></ul>'
        list+='<small><span class=\'material-icons\'>error_outline</span>Esta configuración no podrá cambiarse.</small>'
    }else if(value=='R'){
        list+='<li>Lo usuarios <strong>podrán leer la publicación</strong>, pero <strong>no</strong> podrán escribir continuaciones.</li></ul>'
        list+='<small>Podrás cambiar esta configuración por cualquier otra cuando lo desees.</small>'
    }else if(value=='NR'){
        list+='<li><strong>Solo tú</strong> podrás ver esta publicación.</li></ul>'
        list+='<small>Podrás cambiar esta configuración por cualquier otra cuando lo desees.</small>'
    }
}
return list;
}