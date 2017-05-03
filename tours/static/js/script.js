var nav = document.getElementById("myNav");

function openNav() {
    nav.style.height = "100%";
}

function closeNav() {
    nav.style.height = "0%";
}

$(document).ready(function(){
	$('#nav-icon').click(function(){
		$(this).toggleClass('open');
	});
});

function toggleNav() {
	if (nav.style.height == "100%"){
		closeNav();
	} else {
		openNav();
	}
}

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else {
        window.location = "index.html";
    }
}

function showPosition(position) {
    var latlon = position.coords.latitude + "," + position.coords.longitude;

    var img_url = "https://maps.googleapis.com/maps/api/staticmap?center="
    +latlon+"&zoom=17&size=400x1200&sensor=false&key=AIzaSyBu-916DdpKAjTmJNIgngS6HL_kDIKU0aU";
    document.getElementById("mapholder").innerHTML = "<img src='"+img_url+"'>";
}

function showError(error) {
    switch(error.code) {
        case error.PERMISSION_DENIED:
            window.location = "destinations";
            break;
        case error.POSITION_UNAVAILABLE:
            window.location = "destinations";
            break;
        case error.TIMEOUT:
            window.location = "destinations";
            break;
        case error.UNKNOWN_ERROR:
            x.innerHTML = "An unknown error occurred."
            break;
    }
}