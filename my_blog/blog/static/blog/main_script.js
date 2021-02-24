// progressbar measures height of article
// ToDo exclude comments
$(document).ready(function () {

// navbar and footer hide and seek
var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("navbar").style.top = "0";
    $('.dropdown-menu-nav').removeClass('d-none')
  } else {
    document.getElementById("navbar").style.top = -$('#navbar').outerHeight() + 'px';
    $('.dropdown-menu-nav').addClass('d-none')
  }
  if (prevScrollpos < currentScrollPos) {
    document.getElementById("footer").style.bottom = "0";
  } else {
    document.getElementById("footer").style.bottom = -$('#footer').outerHeight() + 'px';
  }
  prevScrollpos = currentScrollPos;
}


});
