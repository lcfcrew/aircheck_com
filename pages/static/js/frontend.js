

var earth;

var aqi_layer;
var aresol_layer;
var sulfir_layer;
var ozone_layer;

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

    var d = new Date();
    var month = d.getMonth() + 1;
    var day = d.getDay();
    var year = d.getYear();

    aresol_layer = new L.GIBSLayer('MODIS_Combined_Value_Added_AOD', {
        date: new Date(year + '/' + month + '/' + day),
        transparent: true
    }).addTo(earth);

    var options = { bounds: [[35.98245136, -112.26379395],[36.13343831, -112.10998535]],
                    minZoom: 10,
                    maxZoom: 16 };
    var grandcanyon = WE.tileLayer('http://tileserver.maptiler.com/grandcanyon/{z}/{x}/{y}.png', options);
    grandcanyon.addTo(earth);

    var layer = new L.GIBSLayer('MODIS_Aqua_SurfaceReflectance_Bands721', {
        date: new Date('2015/04/01'),
        transparent: true
    }).addTo(earth);


//    var test = new L.GIBSLayer('MODIS_Aqua_SurfaceReflectance_Bands721', {
//    date: new Date('2015/04/01'),
//    transparent: true
//    }).addTo(earth);



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
    getLatLongFromString(location, addNasaMarker);
}

function submitTweet()
{
 var message = document.getElementById('input_message').value;
    alert(message);
}