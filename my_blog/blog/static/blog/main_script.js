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
	
	function tagRenderer(tags){
		$tagSection = $('<div>').addClass('card-body').append(
			$('<label>').text('جستجو در برچسب ها')
		)
		for(tag of tags.results){
			
			$tagSection.append(
				$('<a>').addClass('px-1').text(tag.name).prop('href', `/tags/${tag.name}`)
			)
		}
		$('#search-results').append($tagSection)
	}
	
	
	function topicRenderer(topics){
		$topicSection = $('<div>').addClass('card-body').append(
			$('<label>').text('جستجو در دسته بندی ها')
		)
		for(topic of topics.results){
			
			$topicSection.append(
				$('<a>').addClass('px-1').text(topic).prop('href', `/tags/${topic}`)
			)
		}
		$('#search-results').append($topicSection)
	}
	
	function artRenderer(arts){
		$articleSection = $('<div>').addClass('card-body d-flex flex-column')
		for(art of arts.results){
			
			$articleSection.append(
				$('<a>').addClass('px-1').text(art.title).prop('href', `/@${art.username}/${art.id}`)
			)
		}
		$('#search-results').append($articleSection)
	}
	
	$('#search-bar').keyup(function(event){
			var keycode = (event.keyCode ? event.keyCode : event.which);
			if(keycode>=37 && keycode<=40){
				console.log('salam chetory')
			}
			else{
				$('#search-results').empty()
				if (keycode != 8){
					$.get('/api/search/',{q: $(this).val()},
					function(data){
						console.log(data)
						}
	  				);
  				}
  				
  				$.get('/api/tag/',{name: $(this).val()},
				function(data){
					tagRenderer(data)
					}
  				);
  				
  				$.get('/api/topic/',{name: $(this).val()},
				function(data){
					topicRenderer(data)
					}
  				);
  			}
	});
console.log('hir')
});
