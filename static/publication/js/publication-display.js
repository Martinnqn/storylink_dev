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
            history.pushState(undefined, undefined, url);
            cont = JSON.parse(data.responseText).content_pub;
            if (cont.img_content_link!=undefined){
                $("#header-image").attr('src',cont.img_content_link);
                $("#header-image").attr('alt',cont.own_username);
            }
            $("#img-owner").attr('src',cont.own_user_image);
            $("#img-owner").attr('alt',cont.own_username);
            $("#link-autor-profile").attr('href',cont.url_autor);

            if (cont.active && cont.own_user == user_id){
                $("#btn-edit").attr('href',cont.url_edit);
                $("#btn-delete").attr('href',cont.url_delete);
                $("#card-options-owner").css({'display': 'inline-block'});
            }else{
                $("#btn-edit").attr('href','');
                $("#btn-delete").attr('href','');
                $("#card-options-owner").css({'display': 'none'});
            }

            $("#title-pub-detail").html(cont.title);

            $("#title-read-mode").html(cont.title);
            $("#publication-content").html(cont.text_content);

            if (cont.active){
                if (cont.own_user != user_id){
                        $("#subscribe-story").attr('onclick', `subUnsubToStory('`+cont.url_subscribe+`')`);
                        $("#unsubscribe-story").attr('onclick', `subUnsubToStory('`+cont.url_unsubscribe+`')`);
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

                $("#btn-create-continuation").attr('href',cont.url_continuate);
                $("#btn-create-continuation").css({display:'flex'});

            }else{
                $("#btn-create-continuation").attr('href','javascript: void(0)');
                $("#subscribe-story").attr('onclick', '');
                $("#subscribe-story").attr('onclick', '');
                $("#btn-create-continuation").css({display:'none'});
                $("#subscribe-story").css({display:'none'});
                $("#unsubscribe-story").css({display:'none'});
            }

            $(".displacement-menu").css({'display':"none"});
            
            $("#tags .tags-story").empty();
            if (cont.tags!=undefined){
                for (var i = cont.tags.length - 1; i >= 0; i--) {
                    $("#tags .tags-story").append('<span>'+cont.tags[i]+'</span>'); 
                }
            }

            $("#display-pub-detail").css({
                'display': 'flex',
            });
            showStoriesPreview(cont.url_continuations);
            $("body").css({'overflow-y': 'hidden'});
      }
  });
}


function showInfoChapter(url, user_id, evt) {
    $.ajax({
        url:  url,
        type:  'get',
        dataType:  'text/json',
        complete: function  (data) {
            //console.log(data.responseText);
            cont = JSON.parse(data.responseText).content_pub;
            if (cont.img_content_link!=undefined){
                $("#header-image").attr('src',cont.img_content_link);
                $("#header-image").attr('alt',cont.own_username);
            }
            $("#img-owner").attr('src',cont.own_user_image);
            $("#img-owner").attr('alt',cont.own_username);
            $("#link-autor-profile").attr('href',cont.url_autor);

            if (cont.active && cont.own_user == user_id){
                $("#btn-edit").attr('href',cont.url_edit);
                $("#btn-delete").attr('href',cont.url_delete);
                $("#card-options-owner").css({'display': 'inline-block'});
            }else{
                $("#btn-edit").attr('href','');
                $("#btn-delete").attr('href','');
                $("#card-options-owner").css({'display': 'none'});
            }

            $("#title-pub-detail").html(cont.title);

            $("#title-read-mode").html(cont.question);
            $("#publication-content").html(cont.text_content);

            if (cont.active){
                if (cont.own_first_story != user_id){
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

                $("#btn-create-continuation").attr('href',cont.url_continuate);
                $("#btn-create-continuation").css({display:'flex'});

            }else{
                $("#btn-create-continuation").attr('href','javascript: void(0)');
                $("#subscribe-story").attr('onclick', '');
                $("#subscribe-story").attr('onclick', '');
                $("#btn-create-continuation").css({display:'none'});
                $("#subscribe-story").css({display:'none'});
                $("#unsubscribe-story").css({display:'none'});
            }


            $("#first-story").attr('onclick',`showInfoPub('`+cont.url_first_story+`','`+user_id+`')`); 

            if (cont.url_prev_chapter==null){
                $("#pre-story").attr('onclick',`showInfoPub('`+cont.url_first_story+`','`+user_id+`')`); 
            }else{
                $("#pre-story").attr('onclick',`showInfoChapter('`+cont.url_prev_chapter+`','`+user_id+`')`);
            }

            $(".displacement-menu").css({'display':"flex"});

            $("#tags .tags-story").empty();
            if (cont.tags!=undefined){
                for (var i = cont.tags.length - 1; i >= 0; i--) {
                    $("#tags .tags-story").append('<span>'+cont.tags[i]+'</span>'); 
                }
            }

            $("#display-pub-detail").css({
                'display': 'flex',
            });
            showStoriesPreview(cont.url_continuations);
            $("body").css({'overflow-y': 'hidden'});
      }
  });
}

function hideInfoPub() {
    $("#display-pub-detail").css({
        'opacity': '0',
    })
    setTimeout(function(){ $("#display-pub-detail").css({
        'display': 'none',
        'opacity': '1',
    })}, 450);
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

function showStoriesPreview(url) {
    $.ajax({
        url:  url,
        type:  'get',
        dataType:  'html',
        complete: function  (data) {
            cont = data.responseText;
            $("#scroll-previews").html(cont);
            /*para scrollear hasta el div*/
            /*document.querySelector('#scroll-previews').scrollIntoView({ 
              behavior: 'smooth' 
          });*/
      }
  });
}


function extendStory() {
    //$("#title-read-mode").html($("#publication-title").text())
    $(".content-read-mode").html($("#publication-content").text());
}


function limitText(text, maxLength){
    limite_text = text;
    if (limite_text.length > maxLength)
    {
        limite_text = limite_text.substr(0, maxLength)+" ...";
    }
    return limite_text;
}

/*para salir del search de users*/
$('body').on('keydown', function (e) {
    if (e.which == 27 && !$('#story-read-mode').attr('aria-modal')) {
        hideInfoPub();
    }
});

/*$('#collapsibleNavbarFooter').on('shown.bs.collapse', function () {
  this.scrollIntoView({behavior: 'smooth'});
});*/