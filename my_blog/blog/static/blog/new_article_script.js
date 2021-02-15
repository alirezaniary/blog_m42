
$(document).ready(function () {
// article writing text area resizing
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



// new article page1 validation
// ToDo must include min length 300
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



// tag suggestion key events and ajax
// ToDo refactor to seperate functions
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


// back key functinality new article page2
$('#back').on('click', function(event){  
    $('.new-page1').show();
    $('.new-page2').hide();
});


// image preview new
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
$('#my').click(function(){
$('<link>').attr('rel','stylesheet')
  .attr('type','text/css')
  .attr('href','/static/blog/dark-mode.css')
  .appendTo('head');})
console.log('hdi')

var input = document.getElementById( 'upload' );
var infoArea = document.getElementById( 'upload-label' );

input.addEventListener( 'change', showFileName );
function showFileName( event ) {
var input = event.srcElement;
var fileName = input.files[0].name;
infoArea.textContent = fileName;
}

});