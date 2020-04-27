function animateScroll(target) {
    var x = ($("#theater-main").scrollLeft()+$(target).offset().left)-390;
    $('#theater-main').animate({
        scrollLeft: x,
        //scrollTop: $(target).offset().top
    }, 800);
}
