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
            if (cont.img_content_link!=undefined){
                $("#header-image").attr('src',cont.img_content_link);
                $("#header-image").attr('alt',cont.own_username);
            }
            $("#img-owner").attr('src',cont.own_user_image);
            $("#img-owner").attr('alt',cont.own_username);

            if (cont.active && cont.own_user == user_id){
                $("#btn-edit").attr('href',cont.url_edit);
                $("#btn-delete").attr('href',cont.url_delete);
                $("#card-options-owner").css({'display': 'block'});
            }else{
                $("#btn-edit").attr('href','');
                $("#btn-delete").attr('href','');
                $("#card-options-owner").css({'display': 'none'});
            }

            $("#publication-outer-title").html(cont.title);

            $("#publication-title").html(cont.title);
            $("#publication-content").html(cont.text_content);

            if (cont.active){
                if (cont.own_user != user_id){
                    if (cont.is_subscribed){
                        $("#unsubscribe-story").attr('onclick', `subUnsubToStory('`+cont.url_unsubscribe+`')`);
                        $("#unsubscribe-story").css({display:'inline-block'});
                        $("#subscribe-story").attr('onclick', '');
                        $("#subscribe-story").css({display:'none'});

                    }else{
                        $("#subscribe-story").attr('onclick', `subUnsubToStory('`+cont.url_subscribe+`')`);
                        $("#subscribe-story").css({display:'inline-block'});
                        $("#unsubscribe-story").css({display:'none'});
                        $("#unsubscribe-story").attr('onclick', '');
                    }
                }else{
                    $("#unsubscribe-story").attr('onclick', '');
                    $("#subscribe-story").attr('onclick', '');
                    $("#subscribe-story").css({display:'none'});
                    $("#unsubscribe-story").css({display:'none'});
                }

                $("#create-continuation").attr('href',cont.url_continuate);
                $("#create-continuation").css({display:'block'});

            }else{
                $("#create-continuation").attr('href','javascript: void(0)');
                $("#subscribe-story").attr('onclick', '');
                $("#subscribe-story").attr('onclick', '');
                $("#create-continuation").css({display:'none'});
                $("#subscribe-story").css({display:'none'});
                $("#unsubscribe-story").css({display:'none'});
            }

            $("#pre-story").css({display:"none"})    
            $("#first-story").css({display:"none"})    

            $("#display-pub-detail").css({
                'display': 'block',
            });
            showStoriesPreview(cont.url_continuations);
            $("body").css({'overflow-y': 'hidden'});
            /*para scroll hasta el div*/
            /*document.querySelector('#link-to-body').scrollIntoView({ 
              behavior: 'smooth' 
          });*/
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

            if (cont.active && cont.own_user == user_id){
                $("#btn-edit").attr('href',cont.url_edit);
                $("#btn-delete").attr('href',cont.url_delete);
                $("#card-options-owner").css({'display': 'block'});
            }else{
                $("#btn-edit").attr('href','');
                $("#btn-delete").attr('href','');
                $("#card-options-owner").css({'display': 'none'});
            }


            $("#publication-title").html(cont.question);
            $("#publication-content").html(cont.text_content);

            if (cont.active){
                if (cont.own_user != user_id){
                    if (cont.is_subscribed){
                        $("#unsubscribe-story").attr('onclick', `subUnsubToStory('`+cont.url_unsubscribe+`')`);
                        $("#unsubscribe-story").css({display:'inline-block'});
                        $("#subscribe-story").attr('onclick', '');
                        $("#subscribe-story").css({display:'none'});

                    }else{
                        $("#subscribe-story").attr('onclick', `subUnsubToStory('`+cont.url_subscribe+`')`);
                        $("#subscribe-story").css({display:'inline-block'});
                        $("#unsubscribe-story").css({display:'none'});
                        $("#unsubscribe-story").attr('onclick', '');
                    }
                }else{
                    $("#unsubscribe-story").attr('onclick', '');
                    $("#subscribe-story").attr('onclick', '');
                    $("#subscribe-story").css({display:'none'});
                    $("#unsubscribe-story").css({display:'none'});
                }

                $("#create-continuation").attr('href',cont.url_continuate);
                $("#create-continuation").css({display:'block'});

            }else{
                $("#create-continuation").attr('href','javascript: void(0)');
                $("#subscribe-story").attr('onclick', '');
                $("#subscribe-story").attr('onclick', '');
                $("#create-continuation").css({display:'none'});
                $("#subscribe-story").css({display:'none'});
                $("#unsubscribe-story").css({display:'none'});
            }


            $("#first-story").attr('onclick',`showInfoPub('`+cont.url_first_story+`','`+user_id+`')`); 
            $("#first-story").css({display:"block"});    

            if (cont.url_prev_chapter==null){
                $("#pre-story").attr('onclick',`showInfoPub('`+cont.url_first_story+`','`+user_id+`')`); 
            }else{
                $("#pre-story").attr('onclick',`showInfoChapter('`+cont.url_prev_chapter+`','`+user_id+`')`);
            }
            $("#pre-story").css({display:"block"})   


            $("#display-pub-detail").css({
                'display': 'block',
            });
            showStoriesPreview(cont.url_continuations);
            $("body").css({'overflow-y': 'hidden'});
            /*para scroll hasta el div*/
            /*document.querySelector('#link-to-body').scrollIntoView({ 
              behavior: 'smooth' 
          });*/
      }
  });
}

function hideInfoPub() {
    $("#display-pub-detail").css({'display': 'none'});
    $("#scroll-previews").css({'display': 'none'});
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
            $("#scroll-previews").css({
                display:'flex',
                opacity: '1',
                transition: 'opacity 1s linear',
            });
            /*para scrollear hasta el div*/
            /*document.querySelector('#scroll-previews').scrollIntoView({ 
              behavior: 'smooth' 
          });*/
      }
  });
}


function extendStory() {
    $("#story-data").css({display:'none'});
    $("#display-pub-detail").css({
        'background':'rgba(0,0,0,0.95)',
    });

    $("#publication-container").removeClass("publication-container");
    $("#publication-container").addClass("publication-container-readMode");
    $("#publication-description").removeClass("publication-description");
    $("#publication-description").addClass("publication-description-readMode");

    $("#body-publication").css({'display':'none'});
    $("#title").css({'visibility':'hidden'});

    $("#btnExtend").css({display:'none'});
    $("#btnReduce").css({display:'block'});
}

function reduceStory() {
    $("#display-pub-detail").css({
        'background':'rgba(0,0,0,0.6)',
    });
    $("#story-data").css({display:'block'});
    $("#publication-container").removeClass("publication-container-readMode");
    $("#publication-container").addClass("publication-container");
    $("#publication-description").removeClass("publication-description-readMode");
    $("#publication-description").addClass("publication-description");
    
    $("#body-publication").css({'display':'block',});
    $("#title").css({'visibility':'visible'});

    $("#btnExtend").css({display:'block'});
    $("#btnReduce").css({display:'none'});


}

function limitText(text, maxLength){
    limite_text = text;
    if (limite_text.length > maxLength)
    {
        limite_text = limite_text.substr(0, maxLength)+" ...";
    }
    return limite_text;
}


/*$('#collapsibleNavbarFooter').on('shown.bs.collapse', function () {
  this.scrollIntoView({behavior: 'smooth'});
});*/