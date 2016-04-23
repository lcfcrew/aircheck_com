

var earth;

function initialize() {
    var options = {
        atmosphere: true,
        center: [0, 0],
        zoom: 4,
        zooming: false,
    };
    earth = new WE.map('earth_div', options);
    var natural = WE.tileLayer('/static/img/webgl/{z}/{x}/{y}.jpg', {
        tileSize: 256,
        tms: true
    });
    natural.addTo(earth);


    // Start a simple rotation animation
    var before = null;
    requestAnimationFrame(function animate(now) {
        var c = earth.getPosition();
        var elapsed = before ? now - before : 0;
        before = now;
        earth.setCenter([c[0], c[1] + 0.1 * (elapsed / 30)]);
        requestAnimationFrame(animate);
    });
}

function addNasaMarker( title,  message,  lat,  long)
{
    var marker = WE.marker([lat, long]).addTo(earth);
    var div = nasaMarkerDiv(title, message);

    marker.bindPopup(div, {
        maxWidth: 150,
        closeButton: false
    }).openPopup();

    earth.setView([lat, long], 4);

    return marker;
}

function nasaMarkerDiv( title, message) {
    return "<div class='nasa-marker'><b>" + title + "</b><br>" + message + "<br /></div>";
}

function submitLocation()
{
    var location = document.getElementById('input_location').value;
    var value = getLatLongFromString(location);
    alert(value);
}

function submitTweet()
{
 var message = document.getElementById('input_message').value;
    alert(message);
}