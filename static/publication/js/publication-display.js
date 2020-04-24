//////////////////////////////////////////////////////
///Para la valoracion de la publicacion
//////////////////////////////////////////////////////
var $star_rating = $('.star-rating .fa');

var SetRatingStar = function() {
  return $star_rating.each(function() {
    if (parseInt($star_rating.siblings('input.rating-value').val()) >= parseInt($(this).data('rating'))) {
      return ($(this)).removeClass('not-pressed').addClass('pressed');
  } else {
    return ($(this)).removeClass('pressed').addClass('not-pressed');
}
});
};

$star_rating.on('click', function() {
    $star_rating.siblings('input.rating-value').val(($(this)).data('rating'));
    return SetRatingStar();
});

SetRatingStar();
//////////////////////////////////////////////////////
//////////////////////////////////////////////////////
//////////////////////////////////////////////////////


//////////////////////////////////////////////////////
//////////////////////////////////////////////////////
//////////////////////////////////////////////////////


//recibe un array de tags y los convierte en string html safe.
function makeTags(cont, array) {
    for (var i = array.length - 1; i >= 0; i--) {
        cont.append($("<span></span>").text(array[i]));
    }
}

function hideInfoPub() {
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

/*para salir del modo theater*/
$('body').on('keydown', function (e) {
    if (e.which == 27 && !$('#story-read-mode').attr('aria-modal')) {
        hideInfoPub();
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
            loadTheater(cont, user_id, url, 'story', null);
            $("#display-pub-detail").css({
                'display': 'flex',
            });
            $("body").css({'overflow-y': 'hidden'});
        }
    });
}


function showInfoChapter(url, user_id, idParent, idPrev, evt) {
    $.ajax({
        url:  url,
        type:  'get',
        dataType:  'text/json',
        complete: function  (data) {
            //console.log(data.responseText);
            cont = JSON.parse(data.responseText).content_pub;
            loadTheater(cont, user_id, url, 'chapter', idPrev);
        }
    });
}

/*Clona el template theater-view-template y lo rellena con los datos de la publicacion. 
Discrimina entre publicacion story y chapter.
Cuando encuentra un atributo id, lo modifica agregandole el id de la publicacion (el idPubToIdUnique),
para que no se repitan. Algunos id del theater-mode no son modificados (porque no pertenecen
al div theather-view-template), como la suscripcion a la story principal y el titulo de la story.*/
function loadTheater(cont, user_id, url, typePubli, idParent) {
    history.pushState(undefined, undefined, url+'?mode=theater');
    $("#header-base").removeClass('sticky-top');
    //a la story le concateno main_ porque puede haber un capitulo con el mismo id que la story.
    if (typePubli=='story'){
        pubid = cont.id+"";
    }else{
        pubid = idParent+"_"+cont.id;
    }
    idPubToIdUnique.set(cont.id, pubid);
    updateViews(idParent);
    parentView.set(idPubToIdUnique.get(idParent), pubid);
    newNode = $("#theater-view-template").clone(true);
    $("#theater-main").append(newNode);
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
        $("#first-story_"+pubid).attr('onclick',`showInfoPub('`+cont.url_first_story+`','`+user_id+`')`); 
        if (cont.url_prev_chapter==null){
            $("#pre-story_"+pubid).attr('onclick',`showInfoPub('`+cont.url_first_story+`','`+user_id+`')`); 
        }else{
            $("#pre-story_"+pubid).attr('onclick',`showInfoChapter('`+cont.url_prev_chapter+`','`+user_id+`')`);
        }
        $("#displacement-menu_"+pubid).css({'display':"flex"});
    }

    $("#tags_"+pubid+" .tags-story").empty();
    if (cont.tags!=undefined){
        makeTags($("#tags_"+pubid+" .tags-story"), cont.tags)
    }

    newNode.css({'display':'block'})
    showStoriesPreview(cont.url_continuations, pubid);
}

/*Actualizar las theater-views...*/
function updateViews(idParent) {
    if (idParent!=null){
        idParentUnique = idPubToIdUnique.get(idParent);
        deletChildView(idParentUnique)
    }else{
        console.log("Entraca")
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