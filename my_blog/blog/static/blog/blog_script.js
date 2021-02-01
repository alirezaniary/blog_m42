$(window).scroll(function () {
  var s = $(window).scrollTop(),
        d = $(document).height(),
        c = $(window).height();
        scrollPercent = (s / (d-c)) * 100;
        var position = scrollPercent;

   $("#progressbar").attr('style', 'width: ' + position + '%; transition: none;');

});

var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("navbar").style.top = "0";
    $('.dropdown-menu').removeClass('d-none')
  } else {
    document.getElementById("navbar").style.top = -$('#navbar').outerHeight() + 'px';
    $('.dropdown-menu').addClass('d-none')
  }
  if (prevScrollpos < currentScrollPos) {
    document.getElementById("footer").style.bottom = "0";
  } else {
    document.getElementById("footer").style.bottom = -$('#footer').outerHeight() + 'px';
  }
  prevScrollpos = currentScrollPos;
}

