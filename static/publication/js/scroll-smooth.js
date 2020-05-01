function animateScroll(target) {
    /*console.log($('#theater-main').scrollTop())
    console.log($('#theater-main').offset().top)
    console.log($(target).scrollTop())
    console.log($(target).offset().top)
    console.log("resss")
    console.log($('#theater-main').scrollTop()+($(target).offset().top-window.pageYOffset))
    alert(window.pageYOffset-$(target).offset().top)
    alert($(target).offset().top)*/
    //el scrollTop necesita restarle el pageYoffset porque nose pero funciona.
    $('#theater-main').animate({
        scrollTop: $('#theater-main').scrollTop()+($(target).offset().top-window.pageYOffset),
        scrollLeft: $('#theater-main').scrollLeft()+$(target).offset().left-240,
    }, 800);

}