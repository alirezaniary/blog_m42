$(document).ready(function () {
	// progressbar measures height of article
	// ToDo exclude comment height
	$(window).scroll(function () {
		var s = $(window).scrollTop(),
			duc = $(document).height(),
			c = $(window).height(),
			scrollPercent = (s / (duc-c)) * 100;
		var position = scrollPercent;
		$("#progressbar").attr('style', 'width: ' + position + '%; transition: none;');
	});
	
	function renderLike (status){
		if(status.did_like){
			if(status.is_like){
				$('.like, .dislike-fill').hide()
				$('.like-fill, .dislike').show()
				$('#like-count').text(status.like_count)
				$('#dislike-count').text(status.dislike_count)
			}
			else{
				$('.dislike, .like-fill').hide()
				$('.dislike-fill, .like').show()
				$('#like-count').text(status.like_count)
				$('#dislike-count').text(status.dislike_count)
			}
		}
		else{
			$('.like, .dislike').show()
			$('.like-fill, .dislike-fill').hide()
			$('#like-count').text(status.like_count)
			$('#dislike-count').text(status.dislike_count)
		}
	}
	
	function renderBookmark (status){
		if(status.bookmarked){
			$('.bookmark').hide()
			$('.bookmark-fill').show()
		}
		else{
			$('.bookmark').show()
			$('.bookmark-fill').hide()
		}
	}
	
	var input_data = JSON.parse($('#json').text());
	
	$.getJSON('/api/like/', input_data, function(status){
		renderLike(status);
	});
	
	$.getJSON('/api/bookmark/', input_data, function(status){
		renderBookmark(status);
	});
			
	
	input_data.csrfmiddlewaretoken = $('[name=csrfmiddlewaretoken]').val();

	$('#like-inline, #like-side').click(function(){
			input_data.like = 1

			$.post('/api/like/', input_data, function(status){
				renderLike(status);	
			});
	});
	
	$('#dislike-inline, #dislike-side').click(function(){
			input_data.like = 0

			$.post('/api/like/', input_data, function(status){
				renderLike(status);	
			});
	});
	
	$('.bookmark, .bookmark-fill').click(function(){
			$.post('/api/bookmark/', input_data, function(status){
				renderBookmark(status)
			});
	});
	

console.log('end')
});
