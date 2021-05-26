$( document ).ready(function() {
	$("#toggleButton").on("click", function() {
		document.getElementById("sidebar").classList.toggle('active');
	});

	$("#one").on("click", function() {
		var $url = $('#one').html();
		window.location = $url;
	});

	$("#two").on("click", function() {
		var $url = $('#two').html();
		window.location = $url;
	});

	$("#three").on("click", function() {
		var $url = $('#three').html();
		window.location = $url;
	});

	$( "#link" ).on( "click", function() {
		var $url = $('#link').html();
		window.location = $url;
	});

	$("#home").on("click", function() {
		window.location = "/";
	});

	$("#welcome").on("click", function() {
		window.location = "/welcome";
	});

	$("#about").on("click", function() {
		window.location = "/about";
	});

	$("#cv").on("click", function() {
		window.location = "/cv";
	});

	$("#avatar").on("click", function() {
		window.location = "/avatar";
	});

	$("#personal").on("click", function() {
		window.location = "/personal";
	});

	$("#education").on("click", function() {
		window.location = "/education";
	});

	$("#project").on("click", function() {
		window.location = "/project";
	});
});