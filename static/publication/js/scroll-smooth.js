function animateScroll(target) {
    var x = ($("#theater-main").scrollLeft()+$(target).offset().left)-390;
    var y = ($("#theater-main").scrollTop()+$(target).offset().top);
    $('#theater-main').animate({
        scrollLeft: x,
        scrollTop: y,
        //scrollTop: $(target).offset().top
    }, 800);
}
