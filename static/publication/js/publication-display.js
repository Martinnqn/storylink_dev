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


function showInfoChapter(url, user_id, idParent, evt) {
    $.ajax({
        url:  url,
        type:  'get',
        dataType:  'text/json',
        complete: function  (data) {
            //console.log(data.responseText);
            cont = JSON.parse(data.responseText).content_pub;
            loadTheater(cont, user_id, url, 'chapter', idParent);
        }
    });
}

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
            /*para scrollear hasta el div*/
            /*document.querySelector('#scroll-previews').scrollIntoView({ 
              behavior: 'smooth' 
          });*/
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


var views = [];
var pubsToViews = [];

function loadTheater(cont, user_id, url, typePubli, idParent) {
    history.pushState(undefined, undefined, url+'?mode=theater');
    $("#header-base").removeClass('sticky-top');
    if (typePubli=='story'){
        pubid = 'main_'+cont.id;
    }else{
        if (idParent!=null){
            pubid = idParent;
        }else{
            pubid = cont.id;
        }
    }
    newNode = $("#theater-view-template").clone(true);
    $("#theater-main").append(newNode);
    newNode.attr('id',"theater-view_"+pubid);
    newNode.id="theater-view_"+pubid;

    elements = newNode.find('[id]');

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
            $("#unsubscribe-story_"+pubid).attr('onclick', `subUnsubToStory('`+cont.url_unsubscribe+`')`);
            $("#subscribe-story_"+pubid).attr('onclick', `subUnsubToStory('`+cont.url_subscribe+`')`);
            if (cont.is_subscribed){
                $("#unsubscribe-story_"+pubid).css({display:'inline-block'});
                //$("#subscribe-story").attr('onclick', '');
                $("#subscribe-story_"+pubid).css({display:'none'});

            }else{
                $("#subscribe-story_"+pubid).css({display:'inline-block'});
                $("#unsubscribe-story_"+pubid).css({display:'none'});
                //$("#unsubscribe-story").attr('onclick', '');
            }
        }else{
            $("#unsubscribe-story_"+pubid).attr('onclick', '');
            $("#subscribe-story_"+pubid).attr('onclick', '');
            $("#subscribe-story_"+pubid).css({display:'none'});
            $("#unsubscribe-story_"+pubid).css({display:'none'});
        }

        $("#btn-create-continuation_"+pubid).attr('href',cont.url_continuate);
        $("#btn-create-continuation_"+pubid).css({display:'flex'});

    }else{
        $("#btn-create-continuation_"+pubid).attr('href','javascript: void(0)');
        $("#subscribe-story_"+pubid).attr('onclick', '');
        $("#subscribe-story_"+pubid).attr('onclick', '');
        $("#btn-create-continuation_"+pubid).css({display:'none'});
        $("#subscribe-story_"+pubid).css({display:'none'});
        $("#unsubscribe-story_"+pubid).css({display:'none'});
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

