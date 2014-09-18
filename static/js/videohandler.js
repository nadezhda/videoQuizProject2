$(window).load(function(){

	// GLOBAL VARIABLES
	markerBreaks = [60, 120, 180, 240];

	var video = videojs("my-video");
	
	videojs('my-video').ready(function(){
		this.on("progress", onProgress); // on equial addEvent
		this.on("popup", displayOverlay); // on equial addEvent
	});

	function onProgress() {
		var playAt = video.currentTime();
		var markers = markerBreaks;
		console.log("current time" + playAt);
	    for (i=0; i < markers.length; i++){
	    	var marker = markers[i];
   			console.log("marker time" + marker);
	    	if (playAt >= marker){
			    video.pause();
			    markers.splice(0,1);
			}
   		}		
	}

	function displayOverlay(){
		video.pause();
	}

	// function jumpToTime(){
	//     var video = $("video")[0];
	//     video.pause();
	//     video.currentTime = 160;
	//     video.play();
	// };

	onProgress();
	html = '';

	videojs('my-video').ready(function(){

		// Load markers
		this.markers({
		  setting: {
		    //set style, markertip, and breakOverlay
		    markerStyle: {
		      'width':'8px',
		      'background-color': 'orange'
		    },
		    markerTip:{
		      display: true,
		      default_text: "",
		      show_colon: false
		    },

		    forceInitialization: true // doesn't wait for loadedmetadata event
		  },
		  marker_breaks: markerBreaks,
		  marker_text  :['Question 1','Question 2','Question 3','Question 4']			
		}); //---> end markers

		// Load overlays
		this.overlay({
	      overlays: [{
	        content: fragment,
	        start: 60,
	        end: 'play',
	      }, {
	        content: '<input type="submit" value="Button 2"/>',
	        start: 120,
	        end: 'play',
	        align: 'top-right'
	      }]

		}); //---> end ovelays

	});


	// var answerList = ["Internet Explorer", "Mozilla Firefox", "Safari", "Chrome", "Opera"];
	// var fragment = document.createDocumentFragment();

	// form = document.createElement('div');
	// p = document.createElement('p');
	// form.appendChild(p);
	
	// for(var e=0; e < 5; e++){
	// 	var input = document.createElement("input");
	// 		input.setAttribute('type', 'radio');
	// 		input.setAttribute('name', 'answer');
	// 		input.innerHTML = 'Answer' + e + '<br />';
	// 		form.appendChild(input);
	// }

	// fragment.appendChild(form);

	fragment = "<form class='questionForm'><p><Question 1</p><input type='radio' name='answer' value='a1' /><label for=''a1''>Answer1</label></form>";





 //    for(var x = 0; x < 10; x++) {
	// 	var li = document.createElement("li");
	// 	li.innerHTML = "List item " + x;
	// 	fragment.appendChild(li);
	// }
	
	// buildHTML = function(tag, html, attrs) {
	//   // you can skip html param
	//   if (typeof(html) != 'string') {
	//     attrs = html;
	//     html = null;
	//   }
	//   var h = '<' + tag;
	//   for (attr in attrs) {
	//     if(attrs[attr] === false) continue;
	//     h += ' ' + attr + '="' + attrs[attr] + '"';
	//   }
	//   return h += html ? ">" + html + "</" + tag + ">" : "/>";
	// }




	

});  
