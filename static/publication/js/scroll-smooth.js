function animateScroll(target) {
    var x = $("#theater-main").scrollLeft()+$(target).offset().left;
    x=x-450;
    var x = x;
    $('#theater-main').animate({
        scrollLeft: x,
        //scrollTop: $(target).offset().top
    }, 800);
}