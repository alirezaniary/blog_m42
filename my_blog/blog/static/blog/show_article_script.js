$(document).ready(function () {
	// progressbar measures height of article
	// ToDo exclude comment height
	$(window).scroll(function () {
		var s = $(window).scrollTop(),
			d = $(document).height() - $('.comment').height(),
			c = $(window).height(),
			scrollPercent = (s / (d-c)) * 100;
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
	
	
	function renderComment (status){
		$('#comment-temp').show().children('div').children().text(status.text)
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
	
	$('.comment-btn, .response-btn').click(function(e){
		e.preventDefault()
		for(field of $(this).parent().serializeArray()){
			input_data[field.name] = field.value	
		}
		$(this).siblings('#id_text').val('')

		$.post('/api/comment/', input_data, function(status){
			renderComment(status)
			$('html, body').animate({
				scrollTop: ($('#comment-temp').offset().top-50)
			},500);
		});
	});
	

	function renderClike (status){
		if(status.did_like){
			if(status.is_like){
				$(`#p-${status.id} .clike, #p-${status.id} .disclike-fill`).hide()
				$(`#p-${status.id} .clike-fill, #p-${status.id} .disclike`).show()
				$(`#p-${status.id} #clike-count`).text(status.like_count)
				$(`#p-${status.id} #disclike-count`).text(status.dislike_count)
			}
			else{
				$(`#p-${status.id} .disclike, #p-${status.id} .clike-fill`).hide()
				$(`#p-${status.id} .disclike-fill, #p-${status.id} .clike`).show()
				$(`#p-${status.id} #clike-count`).text(status.like_count)
				$(`#p-${status.id} #disclike-count`).text(status.dislike_count)
			}
		}
		else{
			$(`#p-${status.id} .clike, #p-${status.id} .disclike`).show()
			$(`#p-${status.id} .clike-fill, #p-${status.id} .disclike-fill`).hide()
			$(`#p-${status.id} #clike-count`).text(status.like_count)
			$(`#p-${status.id} #disclike-count`).text(status.dislike_count)
		}
	}
	
	$('.clike-inline').click(function(){
		input_data.like = 1
		id = $(this).prop('id')
		input_data.comment = id
		$.post('/api/clike/', input_data, function(status){
			status.id = id
			renderClike(status);	
		});
	});
	
	$('.disclike-inline').click(function(){
		input_data.like = 0
		id = $(this).prop('id')
		input_data.comment = id
		$.post('/api/clike/', input_data, function(status){
			status.id = id
			renderClike(status);	
		});
	});
	
	$('#follow, #un-follow').click(function(){
		$.post('/api/follow/', input_data, function(status){
			if(status.follow){
				$('#un-follow').show()
				$('#follow').hide()
				$('#followers').text(status.followers)
			}else{
				$('#un-follow').hide()
				$('#follow').show()
				$('#followers').text(status.followers)
			}
		});
	});
console.log('engd')
});
