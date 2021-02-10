$(document).ready(function () {
$(window).scroll(function () {
  var s = $(window).scrollTop(),
        duc = $(document).height(),
        c = $(window).height();
        scrollPercent = (s / (duc-c)) * 100;
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





$('#id_text').keypress(function(event){
    var keycode = (event.keyCode ? event.keyCode : event.which);
    if(keycode == '13'){
    	var row = $(this).attr('row')
		$(this).attr('row', +row + 1)
		if (row > 3 && $(this).attr('rows') < 25){
			var rows = $(this).attr('rows')
			$(this).attr('rows', +rows + 1)
		}
    }
});




$('#continue').on('click', function(e){
  var validator = $('#new-form').validate({
  messages: {
    title: "اوپس!!!",
    text:  "اوپس!!!",
    }
});


  if(validator.form()){
  $('.new-page1').hide();
  $('.new-page2').show();
  }

});


$('#tag-input').keypress(function(event){
    var keycode = (event.keyCode ? event.keyCode : event.which);
    if(keycode == '13'){
    	event.preventDefault()
    	var tagValue = $(this).val()
    	$(this).val("")
    	$('<span class="tag-card badge rounded-pill bg-secondary p-2 m-2">' + tagValue + '</span>')
				.css('cursor', 'pointer')
				.hover(function(){$(this).addClass('shadow');}, function(){$(this).removeClass('shadow');})
				.click(function(){$('#id_tag option:contains(' + $(this).text() + ')').remove();
								  $(this).remove();})
				.insertBefore($(this));
		$.post('/api/tag/',{tag: tagValue,
							csrfmiddlewaretoken: $('[name=csrfmiddlewaretoken]').val()},
		function(data){
			$('<option value=' + data.id + '>' + data.name + '</option>')
					.appendTo('#id_tag')
			
		
		}
		);
		}});
		
$('#tag-input').keyup(function(event){
			var keycode = (event.keyCode ? event.keyCode : event.which);
			if(keycode>=37 && keycode<=40){
			console.log('salam chetory')}else{
			$('#datalistOptions').empty();
			$.getJSON('/api/tag/',{tag: $(this).val()},
			function(data){
				for(option of data){
					$('<option value=' + option.name + ' >')
					.appendTo('#datalistOptions')
				}

  			})}

});




$('#back').on('click', function(event){  
    $('.new-page1').show();
    $('.new-page2').hide();
});


function readURL(input) {
  if (input.files && input.files[0]) {
      var reader = new FileReader();

      reader.onload = function (e) {
          $('#imageResult')
              .attr('src', e.target.result);
      };
      reader.readAsDataURL(input.files[0]);
  }
}

$('#upload').on('change', function () {
    readURL(input);
});


var input = document.getElementById( 'upload' );
var infoArea = document.getElementById( 'upload-label' );

input.addEventListener( 'change', showFileName );
function showFileName( event ) {
var input = event.srcElement;
var fileName = input.files[0].name;
infoArea.textContent = fileName;
}


console.log('hdi')
});
