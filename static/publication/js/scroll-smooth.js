function animateScroll(target) {
    /*var x = ($("#theater-main").scrollLeft()+$(target).offset().left)-390;
    var y = ($("#theater-main").scrollTop()+$(target).offset().top);
    $('#theater-main').animate({
        scrollLeft: x,
        //scrollTop: $(target).offset().top
    }, 800);*/
    console.log($('#theater-main').scrollTop())
    console.log($(target).scrollTop())
    console.log($(target).offset().top)
    $('#theater-main').animate({
        scrollTop: $('#theater-main').scrollTop()+$(target).offset().top-280,
        scrollLeft: $('#theater-main').scrollLeft()+$(target).offset().left-280,
    }, 800);
}


$(document).ready(function(){
  // Add smooth scrolling to all links
  $("a").on('click', function(event) {

    // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
      // Prevent default anchor click behavior
      event.preventDefault();

      // Store hash
      var hash = this.hash;

      // Using jQuery's animate() method to add smooth page scroll
      // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 800, function(){

        // Add hash (#) to URL when done scrolling (default click behavior)
        window.location.hash = hash;
      });
    } // End if
  });
});

