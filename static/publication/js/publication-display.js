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
            //$("#publication-container-title #title").html('<h4>'+cont.user_name+' '+cont.user_lastname+'-Story</h4>');
            if (cont.img_content_link!=undefined){
                $("#content-image #img").html('<img alt="Publication image" class="img-thumbnail mx-auto d-block" src="'+cont.img_content_link+'">');
                //$("#content-image #img").html('<img alt="Publication image" class="img-thumbnail mx-auto d-block" src="/../../static/imgs/img1.png">');
            }
            $("#autor").html('<p>Autor: <a href="/user/'+cont.own_username+'/">'+cont.own_username+'</a></p>');

            if (cont.active && cont.own_user == user_id){
                $("#pub-owner").css({'display': 'block'});
                $("#pub-owner").html("<p><a class='btn-edit' href='/user/"+cont.own_username+"/publication/edit-story/"+cont.id+"'>Editar</a>"+
                    "<a class='btn-delete' href='/user/"+cont.own_username+"/publication/delete-story/"+cont.id+"'>Eliminar</a></p>");
            }else{
                $("#pub-owner").css({'display': 'none'});
                $("#pub-owner").html('');
            }
            $("#title").html('<h4>'+limitText(cont.title, 35)+'</h4>');
            console.log("text content "+cont.text_content)
            $("#publication-description").html('<h4>'+cont.title+'</h4> <p>'+cont.text_content+'</p>');
            $("#valoration").html(`<p>Valoración: `+cont.valoration+`</p>`);
            if (cont.active){
                $("#subscribe-story").attr('onclick', `subUnsubToStory('/user/`+cont.own_username+`/publication/subscribe/`+cont.id+`')`);
                $("#unsubscribe-story").attr('onclick', `subUnsubToStory('/user/`+cont.own_username+`/publication/unsubscribe/`+cont.id+`')`);
                if (cont.own_user != user_id){
                    if (cont.is_subscribed){
                        $("#unsubscribe-story").css({display:'inline-block'});
                        $("#subscribe-story").css({display:'none'});

                    }else{
                        $("#subscribe-story").css({display:'inline-block'});
                        $("#unsubscribe-story").css({display:'none'});
                    }
                }else{
                    $("#subscribe-story").css({display:'none'});
                    $("#unsubscribe-story").css({display:'none'});
                }

                $(".star-rating").css({display:'block'});
                $("#share-story").css({display:'block'});

                $("#create-continuation").css({display:'block'});
                $("#create-continuation").attr('href','/user/'+cont.own_username+'/publication/'+cont.id+'/create-story');

            }else{
                $("#create-continuation").css({display:'none'});
                $("#subscribe-story").css({display:'none'});
                $("#unsubscribe-story").css({display:'none'});
                $(".star-rating").css({display:'none'});
                $("#share-story").css({display:'none'});
            }

            $("#pre-story").css({display:"none"})    
            $("#first-story").css({display:"none"})    

            $("#display-pub-detail").css({
                'display': 'block',
            });
            showStoriesPreview('/user/'+cont.own_username+'/publication/continuations/'+cont.id);
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
            //$("#publication-container-title #title").html('<h4>'+cont.user_name+' '+cont.user_lastname+'-Story</h4>');
            if (cont.img_content_link!=undefined){
                $("#content-image #img").html('<img alt="Publication image" class="img-thumbnail mx-auto d-block" src="'+cont.img_content_link+'">');
                //$("#content-image #img").html('<img alt="Publication image" class="img-thumbnail mx-auto d-block" src="/../../static/imgs/img1.png">');
            }
            $("#autor").html('<p>Autor: <a href="/user/'+cont.own_username+'/">'+cont.own_username+'</a></p>');

            $("#title").html('<h4>'+limitText(cont.title, 35)+'</h4>');
            $("#publication-description").html('<h4>'+cont.title+'</h4> <p>'+cont.text_content+'</p>');
            $("#valoration").html(`<p>Valoración: `+cont.valoration+`</p>`);
            
            if (cont.active){
                if (cont.own_user == user_id){
                    $("#pub-owner").css({'display': 'block'});
                    $("#pub-owner").html("<p><a class='btn-edit' href='/user/"+cont.own_username+"/publication/edit-chapter/"+cont.id+"'>Editar</a>"+
                        "<a class='btn-delete' href='/user/"+cont.own_username+"/publication/delete-chapter/"+cont.id+"'>Eliminar</a></p>");
                }else{
                    $("#pub-owner").css({'display': 'none'});
                    $("#pub-owner").html('');
                }
                $("#subscribe-story").css({display:'none'});
                $("#unsubscribe-story").css({display:'none'});

                $(".star-rating").css({display:'block'});
                $("#share-story").css({display:'block'});

                $("#create-continuation").css({display:'block'});
                $("#create-continuation").attr('href','/user/'+cont.own_username+'/publication/'+cont.mainStory+'/'+cont.id+'/create-story');

            }else{
                $("#create-continuation").css({display:'none'});
                $("#subscribe-story").css({display:'none'});
                $("#unsubscribe-story").css({display:'none'});
                $(".star-rating").css({display:'none'});
                $("#share-story").css({display:'none'});
            }

            $("#pre-story").css({display:"block"})   

            $("#first-story").attr('onclick',`showInfoPub('/user/`+cont.own_username+`/publication/story-content/`+cont.mainStory+`',`+user_id+`)`); 
            $("#first-story").css({display:"block"})    

            if (cont.prevChapter==null){
                $("#pre-story").attr('onclick',`showInfoPub('/user/`+cont.own_username+`/publication/story-content/`+cont.mainStory+`',`+user_id+`)`);
            }else{
                $("#pre-story").attr('onclick',`showInfoChapter('/user/`+cont.own_username+`/publication/chapter-content/`+cont.prevChapter+`',`+user_id+`)`);
            }

            $("#display-pub-detail").css({
                'display': 'block',
            });
            showStoriesPreview('/user/'+cont.own_username+'/publication/continuations-chapter/'+cont.id);
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