//$(window).load(function(){

	// GLOBAL VARIABLES
	//-------------------------------------
//	markerBreaks = []; // points of markers' location
//	replayTime = []; // time to return to
//	removedMarkers = []; // Markers which is already passed
//    var questionParameterField = document.getElementById("run-replaytime");

    // Get and parse markerTime and replayTIme parameters from hidden div
//    var paramFieldValues = $( "div#run-replaytime" ).text().slice( 0, -1 );
//    var parameters = '['+ paramFieldValues + ']';
//    var obj  = $.parseJSON(parameters);
//
//    for (var i=0; i< obj.length; i++){
//        markerBreaks.push(parseInt(obj[i].markertime));
//        replayTime.push(parseInt(obj[i].replaytime));
//    }
	//-------------------------------------

//	var video = videojs("my-video");
//	var overlay= document.getElementById('video-overlay');
//	var controlBar = document.getElementsByClassName('vjs-control-bar')[0];
//	var replayButton = document.getElementById('replay-btn');
//	var answerButton = document.getElementById('answer-btn');
//	var skipButton = document.getElementById('skip-btn');
//
//	 skipButton.addEventListener('click',function(e){
//	 	video.play();
//	 	overlay.style.display= 'none';
//	 	controlBar.style.display='block';
//
//	 });
//
//	replayButton.addEventListener('click',function(e){
//        for(var i=0; i < replayTime.length; i++){
//            video.currentTime(replayTime[i]);
//            video.play();
//            overlay.style.display= 'none';
//            controlBar.style.display='block';
//        }
////		video.currentTime(replayTime);
////	 	video.play();
////	 	overlay.style.display= 'none';
////	 	controlBar.style.display='block';
//
//	 });
//
//
//	videojs('my-video').ready(function(){
//		this.on("progress", onProgress); // on equial addEvent
//	});
//
//	function onProgress() {
//		/**
//		* --------------------------------------------------
//		* Go through the video play with markers and ovelay
//		* ---------------------------------------------------
//		*/
//		var markers = markerBreaks;
//		var curTime = video.currentTime();
//		console.log("current time =" + curTime);
//
//		// if user jump to previous parts of the video,
//		// return removed earlier markers
//		for(var j=0; j < removedMarkers.length; j++){
//			if(curTime <= removedMarkers[j]){
//				markers.unshift(removedMarkers.splice(0,1));
//			}
//		}
//		console.log("updated removed markers  =" + removedMarkers);
//		console.log("updated markers =" + markers);
//
//	    // if marker is found, pause the video and display overlay
//	    for (var i=0; i < markers.length; i++){
//	    	var marker = markers[i];
//   			console.log("marker time = " + marker);
//
//	    	// If marker found
//	    	if (curTime >= marker){
//			    video.pause();
//			    if(Math.round(curTime) == marker){
//                  //  $( "div#question-title" ).append(questionTitle);
//			    	console.log('Overlay should show up');
//				 	controlBar.style.display='none';
//					overlay.style.display= 'block';
//			    }
//			    else{
//			    	overlay.style.display= 'none';
//			    }
//			    removedMarkers.unshift(markers.splice(0,1)); //TODO
//			    	console.log("removed markers = " + removedMarkers + '(' + removedMarkers.length + ')');
//			}
//
//			// if markers do not exist, play video
//			if(marker.length == 0){
//				video.play();
//			}
//   		}
//	}
//
//	// function jumpToTime(){
//	//     var video = $("video")[0];
//	//     video.pause();
//	//     video.currentTime = 160;
//	//     video.play();
//	// };
//
//	onProgress();
//
//	videojs('my-video').ready(function(){
//
//		// Load markers
//		this.markers({
//		  setting: {
//		    //set style, markertip, and breakOverlay
//		    markerStyle: {
//		      'width':'8px',
//		      'background-color': 'orange'
//		    },
//		    markerTip:{
//		      display: true,
//		      default_text: "",
//		      show_colon: false
//		    },
//
//		    forceInitialization: true // doesn't wait for loadedmetadata event
//		  },
//		  marker_breaks: markerBreaks,
//		  marker_text  :['Question 1','Question 2','Question 3','Question 4'] //TODO
//		}); //---> end markers
//
//		// videojs('my-video	', {}, function() {
//		//   this.seek({ 'seek_param': 'time' })
//		// });
//
//	});
//
//
//
//
//});
