var isTheaterOn = false;
var first_story;
function showTheater() {
    if (!isTheaterOn){
        isTheaterOn = true;
        $("#display-pub-detail").css({
            'display': 'flex',
        });
        $("body").css({'overflow-y': 'hidden'});
    }
}

function hideTheater() {
    isTheaterOn = false;
    $("#display-pub-detail").css({
        'opacity': '0',
    })
    setTimeout(function(){ $("#display-pub-detail").css({
        'display': 'none',
        'opacity': '1',
    })}, 450);
    deleteAllViews();
    $("#header-base").addClass('sticky-top');
    $("body").css({'overflow-y': 'scroll'});
}

/*para salir del modo theater*/
$('body').on('keydown', function (e) {
    if (e.which == 27 && !$('#story-read-mode').attr('aria-modal')) {
        hideTheater();
    }
});


function subUnsubToStory(url) {
    //console.log(url)
    $.ajax({
        url:  url,
        type:  'get',
        dataType:  'text/json',
        complete: function  (data) {
            cont = JSON.parse(data.responseText);
            if (cont.is_subscribed){
                $("#unsubscribe-story").css({display:'inline-block'});
                $("#subscribe-story").css({display:'none'});

            }else{
                $("#subscribe-story").css({display:'inline-block'});
                $("#unsubscribe-story").css({display:'none'});
            }
        }
    });
}

function showStoriesPreview(url, pubid) {
    $.ajax({
        url:  url,
        type:  'get',
        dataType:  'html',
        complete: function  (data) {
            cont = data.responseText;
            $("#scroll-previews_"+pubid).html(cont);
        }
    });
}

/*Para mostrar el modo teatro si se visita una publicacion invocando el get.*/
$(document).ready(function() {
    var params = getParameters();
    for (var i = params.length - 1; i >= 0; i--) {
        if (params[i][0]=='mode' && params[i][1]=='theater'){
            if (location.pathname.split('/')[4]){
                if (location.pathname.split('/')[5]){
                    if (js_user_id){
                        if (location.pathname.split('/')[4]=='chapter-content'){
                            showInfoChapter(location.pathname, js_user_id, null);
                        }else if (location.pathname.split('/')[4]=='story-content')
                        showInfoPub(location.pathname, js_user_id);
                    }
                }
            }
        }
    }
});

/*Variables globales para administrar el comportamiento de las views. 
idPubToIdUnique: dado el id de una publicacion, guardar un id especial usado unicamente en la interfaz.
El id especial es para hacer los id unicos, porque puede darse el caso que una story tenga el mismo id 
que un chapter.
Para la story principal el nuevo id se mantiene igual; para los chapters el nuevo id se forma 
concatenando el id de su storyMain junto con el id del chapter (mainStory id = 1, chapter id= 2, newID = 1_2).

Caso de uso normal: sea P una publicacion con su lista de continuaciones 'A', 'B', ..., Si se clickea 
sobre 'A', luego sobre una continuacion 'A1' de 'A', y luego sobre 'B', se tienen que eliminar todas
las views que siguen a la continuacion 'A' (es decir A1), y actualizar la view 'A' con el contenido de 'B'.
Para esto, tomar el id de la publicacion P, obtener el IDunico desde idPubToIdUnique (como es una story
es el mismo), y recorrer parentView eliminando todas las views que pueden alcanzarse (metodo deletChildView()).
*/
var idPubToIdUnique = new Map();
var parentView = new Map(); //idPubUnique1 -> idPubUnique2 (para saber que idPubUnique1 es padre de una ventana con idPubUnique2)

function deleteAllViews() {
    idPubToIdUnique.forEach(function (value, key) {
        $("#theater-view_"+value).remove();
    });
    idPubToIdUnique.clear();
    parentView.clear();
}

function showInfoPub(url, user_id, evt) {
    $.ajax({
        url:  url,
        type:  'get',
        dataType:  'text/json',
        complete: function  (data) {
            //console.log(data.responseText);
            cont = JSON.parse(data.responseText).content_pub;
            loadTheater(cont, user_id, url, 'story', null, true);
            showTheater();
            first_story = cont.id;
        }
    });
}

/*
//como extra tambien eliminamos cualquier view  que tenga como padre a undefined.
    //ocurre cuando se visita un chapter desde la url.
    deletChildView(undefined);*/

    function showInfoChapter(url, user_id, evt) {
        $.ajax({
            url:  url,
            type:  'get',
            dataType:  'text/json',
            complete: function  (data) {
            //console.log(data.responseText);
            cont = JSON.parse(data.responseText).content_pub;
            loadTheater(cont, user_id, url, 'chapter', cont.previous_pub_id, true);
            showTheater();
        }
    });
    }

    function preLoadPrevChapTheaterView(urlPrevChapt, urlFirstStory, currentView, user_id, all) {
        deleteAllViews();
        loadPrevChapTheaterView(urlPrevChapt, urlFirstStory, currentView, user_id, all);
    }

    function loadPrevChapTheaterView(urlPrevChapt, urlFirstStory, currentView, user_id, all) {
        url =  urlPrevChapt
    // es == "null" y no == null porque asi interpreta javascript un dato que se genera con {'url_prev_chapter': None} en python.
    if (url == "null" || url == null){ 
        url =  urlFirstStory
    }
    $.ajax({
        url:  url,
        type:  'get',
        dataType:  'text/json',
        complete: function  (data) {
            //console.log(data.responseText);
            cont = JSON.parse(data.responseText).content_pub;
            var IdNewView;
            if (cont.previous_pub_id != undefined){
                IdNewView = loadTheater(cont, user_id, url, 'chapter', cont.previous_pub_id, false);
                parentView.set(IdNewView, currentView);
                if (all){
                    loadPrevChapTheaterView(cont.url_prev_chapter, cont.url_first_story, IdNewView, user_id, all);
                }
            }else{
                IdNewView = loadTheater(cont, user_id, url, 'story', null, false);
                parentView.set(IdNewView, currentView);
                first_story = cont.id;
                /*Actualizamos es boton para que ya no cargue de nuevo la first-story*/
                idPubToIdUnique.forEach(function (value, key) {
                    $("#first-story_"+value).attr('onclick',''); 
                    $("#first-story_"+value).attr('href',"#theater-view_"+idPubToIdUnique.get(cont.id)); 
                });
            }
            $("#pre-story_"+currentView).attr('onclick',''); 
            $("#pre-story_"+currentView).attr('href',"#theater-view_"+IdNewView); 
        }
    });
}

/*Clona el template theater-view-template y lo rellena con los datos de la publicacion. 
Discrimina entre publicacion story y chapter.
Cuando encuentra un atributo id, lo modifica agregandole el id de la publicacion (el idPubToIdUnique),
para que no se repitan. Algunos id del theater-mode no son modificados (porque no pertenecen
al div theather-view-template), como la suscripcion a la story principal y el titulo de la story.*/
/*Position indica si debe cargarse el nuevo theater a la derecha o izquierda*/
function loadTheater(cont, user_id, url, typePubli, idParent, position) {
    history.pushState(undefined, undefined, url+'?mode=theater');
    $("#header-base").removeClass('sticky-top');
    //a la story le concateno main_ porque puede haber un capitulo con el mismo id que la story.
    if (typePubli=='story'){
        pubid = cont.id+"";
    }else{
        pubid = cont.id_main_story+"_"+cont.id;
    }
    idPubToIdUnique.set(cont.id, pubid);
    updateViews(idParent);
    if (idPubToIdUnique.has(idParent)){
        parentView.set(idPubToIdUnique.get(idParent), pubid);
    }
    newNode = $("#theater-view-template").clone(true);
    if (position){
        $("#theater-main").append(newNode);
    }else{
        $("#theater-main").prepend(newNode);
    }
    newNode.attr('id',"theater-view_"+pubid);
    newNode.id="theater-view_"+pubid;

    elements = newNode.find('[id]');

    /*Actualizar el id de los elementos dentro de newNode para que coincidan con el id de la publicacion*/
    for (var i = elements.length - 1; i >= 0; i--) {
        oldid =elements[i].id;
        elements[i].id = oldid+"_"+pubid;
    }

    if (cont.img_content_link!=undefined && !cont.img_content_link.includes('gallery/no-img.png')){
        $("#header-image_"+pubid).attr('src',cont.img_content_link);
        $("#header-image_"+pubid).attr('alt',cont.own_username);
    }else{
        $("#header-image_"+pubid).css('background', cont.color);
    }
    $("#img-owner_"+pubid).attr('src',cont.own_user_image);
    $("#img-owner_"+pubid).attr('alt',cont.own_username);
    $("#link-autor-profile_"+pubid).attr('href',cont.url_autor);

    if (cont.active && cont.own_user == user_id){
        $("#btn-edit_"+pubid).attr('href',cont.url_edit);
        $("#btn-delete_"+pubid).attr('href',cont.url_delete);
        $("#card-options-owner_"+pubid).css({'display': 'inline-block'});
    }else{
        $("#btn-edit_"+pubid).attr('href','');
        $("#btn-delete_"+pubid).attr('href','');
        $("#card-options-owner_"+pubid).css({'display': 'none'});
    }

    if (typePubli == 'story'){
        $("#title-pub-detail").text(cont.title);
        $("#title-read-mode").text(cont.title);
    }else{
        $("#answer-chapter_"+pubid).text(cont.question);
        $("#title-read-mode").text(cont.question);
        //$("#publication-title_"+pubid).text(cont.question);
    }
    $("#publication-content_"+pubid).html(cont.text_content);
    $(".content-read-mode").html(cont.text_content);

    if (cont.active){
        if ((typePubli == 'story' && cont.own_user != user_id) || (typePubli == 'chapter' && cont.own_first_story != user_id)){
            $("#unsubscribe-story").attr('onclick', `subUnsubToStory('`+cont.url_unsubscribe+`')`);
            $("#subscribe-story").attr('onclick', `subUnsubToStory('`+cont.url_subscribe+`')`);
            if (cont.is_subscribed){
                $("#unsubscribe-story").css({display:'inline-block'});
                //$("#subscribe-story").attr('onclick', '');
                $("#subscribe-story").css({display:'none'});

            }else{
                $("#subscribe-story").css({display:'inline-block'});
                $("#unsubscribe-story").css({display:'none'});
                //$("#unsubscribe-story").attr('onclick', '');
            }
        }else{
            $("#unsubscribe-story").attr('onclick', '');
            $("#subscribe-story").attr('onclick', '');
            $("#subscribe-story").css({display:'none'});
            $("#unsubscribe-story").css({display:'none'});
        }

        $("#btn-create-continuation_"+pubid).attr('href',cont.url_continuate);
        $("#btn-create-continuation_"+pubid).css({display:'flex'});

    }else{
        $("#btn-create-continuation_"+pubid).attr('href','javascript: void(0)');
        $("#subscribe-story").attr('onclick', '');
        $("#subscribe-story").attr('onclick', '');
        $("#btn-create-continuation_"+pubid).css({display:'none'});
        $("#subscribe-story").css({display:'none'});
        $("#unsubscribe-story").css({display:'none'});
    }

    if (typePubli == 'story'){
        $("#displacement-menu_"+pubid).css({'display':"none"});
    }else{
        $("#first-story_"+pubid).attr('onclick',`preLoadPrevChapTheaterView('`+cont.url_prev_chapter+`','`+cont.url_first_story+`','`+pubid+`','`+user_id+`',`+true+`)`); 
        //si tiene al idParent es porque el padre ya estaba creado,
        //por lo que la pre-story no es necesaria cargarla de nuevo (un poco de acoplamiento).
        if(!idPubToIdUnique.has(idParent)){
            if (cont.url_prev_chapter==null){
                //$("#pre-story_"+pubid).attr('onclick',`showInfoPub('`+cont.url_first_story+`','`+user_id+`')`); 
                $("#pre-story_"+pubid).attr('onclick',`loadPrevChapTheaterView('`+cont.url_prev_chapter+`','`+cont.url_first_story+`','`+pubid+`','`+user_id+`',`+false+`)`);
            }else{
                $("#pre-story_"+pubid).attr('onclick',`loadPrevChapTheaterView('`+cont.url_prev_chapter+`','`+cont.url_first_story+`','`+pubid+`','`+user_id+`',`+false+`)`);
            }
        }else{
            $("#pre-story_"+pubid).attr('href',"#theater-view_"+idPubToIdUnique.get(idParent)); 
        }
        $("#displacement-menu_"+pubid).css({'display':"flex"});
    }

    $("#tags_"+pubid+" .tags-story").empty();
    if (cont.tags!=undefined){
        makeTags($("#tags_"+pubid+" .tags-story"), cont.tags)
    }

    newNode.css({'display':'block'})
    showStoriesPreview(cont.url_continuations, pubid);
    return pubid;
}

/*Actualizar las theater-views...*/
function updateViews(idParent) {
    if (idParent!=null){
        idParentUnique = idPubToIdUnique.get(idParent);
        deletChildView(idParentUnique)
    }else{
        //console.log("Entraca")
    }
}

function deletChildView(idParentUnique) {
    childView = parentView.get(idParentUnique);
    if(childView){
        $("#theater-view_"+childView).remove();
        parentView.delete(idParentUnique);
        deletChildView(childView);
    }else{
        //console.log(idParentUnique+" dio child false");
    }
}

//recibe un array de tags y los convierte en string html safe.
function makeTags(cont, array) {
    for (var i = array.length - 1; i >= 0; i--) {
        cont.append($("<span></span>").text(array[i]));
    }
}


function extendStory() {
    //$("#title-read-mode").html($("#publication-title").text())
    //$(".content-read-mode").html($("#publication-content").text());
}


function limitText(text, maxLength){
    limite_text = text;
    if (limite_text.length > maxLength)
    {
        limite_text = limite_text.substr(0, maxLength)+" ...";
    }
    return limite_text;
}


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