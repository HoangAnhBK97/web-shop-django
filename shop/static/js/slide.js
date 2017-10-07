$(function() {
    $('.neoslideshow img:gt(0)').hide();
    setInterval(function(){
      $('.neoslideshow :first-child').fadeOut()
         .next('img').fadeIn()
         .end().appendTo('.neoslideshow');}, 
      4000);
})