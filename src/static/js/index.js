var recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition || window.mozSpeechRecognition || window.msSpeechRecognition)();
recognition.lang = 'en-US';
recognition.interimResults = false;
recognition.maxAlternatives = 5;

function getBotResponse(rawText=null) {
	if (rawText === null) {
    	rawText = $("#textInput").val();
	}
	$("#textInput").val("");
	console.log(window.URL+"/response?msg="+rawText)
	window.location.replace(window.URL+"/response?msg="+rawText);
}
			
$("#textInput").keypress(function(e) {
    if(e.which == 13) {
		getBotResponse();
    }
});

$("#speechInput").click(function() {
	recognition.start();
	recognition.onresult = function(event) {
		getBotResponse(event.results[0][0].transcript);
	};
})
