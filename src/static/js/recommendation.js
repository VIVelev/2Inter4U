var recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition || window.mozSpeechRecognition || window.msSpeechRecognition)();
recognition.lang = 'en-US';
recognition.interimResults = false;
recognition.maxAlternatives = 5;
			
$("#btn_back").click(function() {
    recognition.start();
	recognition.onresult = function(event) {
		console.log(event.results[0][0].transcript);
	};
});
