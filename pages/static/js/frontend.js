

var earth;
var dates = ['2016-04-12', '2016-04-13','2016-04-14','2016-04-15','2016-04-16','2016-04-17','2016-04-18','2016-04-19','2016-04-20', '2016-04-21', '2016-04-22'];


//var aqi_layer;
//var aresol_layer;
//var sulfir_layer;
//var ozone_layer;

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
        maxZoom: 3,
        tms: true
    });
    natural.addTo(earth);


//     Start a simple rotation animation
    var before = null;
    requestAnimationFrame(function animate(now) {
        var c = earth.getPosition();
        var elapsed = before ? now - before : 0;
        before = now;
        earth.setCenter([c[0], c[1] + 0.1 * (elapsed / 30)]);
        requestAnimationFrame(animate);
    });
}

function mapCarbonMonoxide()
{
    for (i = 0; i < 10; i++) {
        var date = dates[i];
        var test = WE.tileLayer('http://map1.vis.earthdata.nasa.gov/wmts-webmerc/MLS_CO_215hPa_Day/default/' + date + '/GoogleMapsCompatible_Level6/{z}/{y}/{x}.png', {
            tileSize: 256,
            tms: false,
            maxZoom: 2,
            opacity: 1
         });
        test.addTo(earth);
    }
}

function mapSulfurDioxide()
{
    for (i = 0; i < 1; i++) {
        var date = dates[i];
        var test = WE.tileLayer('http://map1.vis.earthdata.nasa.gov/wmts-webmerc/MLS_SO2_147hPa_Day/default/' + date + '/GoogleMapsCompatible_Level6/{z}/{y}/{x}.png', {
            tileSize: 256,
            tms: false,
            maxZoom: 1,
            opacity: .3
         });
        test.addTo(earth);
    }
}

function mapDustScore()
{
    for (i = 0; i < 5; i++) {
        var date = dates[i];
        var test = WE.tileLayer('http://map1.vis.earthdata.nasa.gov/wmts-webmerc/AIRS_Dust_Score/default/' + date + '/GoogleMapsCompatible_Level6/{z}/{y}/{x}.png', {
            tileSize: 256,
            tms: false,
            maxZoom: 1,
            opacity: .3
         });
        test.addTo(earth);
    }
}

function mapOzone()
{
    for (i = 0; i < 10; i++) {
        var date = dates[i];
        var test = WE.tileLayer('http://map1.vis.earthdata.nasa.gov/wmts-webmerc/MLS_O3_46hPa_Day/default/' + date + '/GoogleMapsCompatible_Level6/{z}/{y}/{x}.png', {
            tileSize: 256,
            tms: false,
            maxZoom: 1,
            opacity: .3
         });
        test.addTo(earth);
    }
}

function mapDestroyLayers()
{
    alert("boom!");
    WE.remove(earth);
//    earth.remove();
//    initialize();
//    for earth.eachLayer(removeIfNotNatural(this));
}
//
//function removeIfNotNatural()
//{
//    if
//}

//
//
///default/{Time}/{TileMatrixSet}/{TileMatrix}/{TileRow}/{TileCol}.png
//
//http://map1.vis.earthdata.nasa.gov/wmts-webmerc/AIRS_Dust_Score/default/{Time}/{TileMatrixSet}/{TileMatrix}/{TileRow}/{TileCol}.png"
//
//http://map1.vis.earthdata.nasa.gov/wmts-webmerc/MLS_O3_46hPa_Day/default/{Time}/{TileMatrixSet}/{TileMatrix}/{TileRow}/{TileCol}.png"
//


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
function toggler(divId) {
    $("#" + divId).toggle();
}

function submitTweet()
{
 var message = document.getElementById('input_message').value;

//// Convert data to JSON string
//   data = JSON.stringify(message);
//
//   // Submit PUT request
//   $.ajax({
//       url: 'http://127.0.0.1:8000/api/v1/sentiments/',
//       type: 'PUT',
//       dataType: 'json',
//       data: data
//   })
//       .complete(function (data, status) {
//           data.responseText = JSON.parse(data.responseText);
//           complete(data, status)
//       })
}

function submitTweetCallback(data, status)
{
//alert("callback" + data.responseText['text']);
// var data = { 'text': "TestMessage", 'sentiment' : .5, 'lat' : 34, 'long' : -118 };
 var locationName = "Pasadena, CA";
    addNasaMarker(locationName, data.responseText['text'], 34, -118);

    style = calcColorFromScore(4);
    $('#aqi_div').css({'color': '#000', 'background-color': style[1], 'position': 'relative'}); //The specific CSS changes after the first one, are, of course, just examples.
    $('#aqi_div_text').text(locationName + " is " + style[0] + " today");
}

function calcColorFromScore(aqi)
{
    if (aqi < 50) { return ["Good", "#00E400"]; }
    else if (aqi < 100) {return ["Moderate", "#FFFF00"];}
    else if (aqi < 150) {return ["Unhealthy for Sensitive Groups", "#FF7E00"];}
    else if (aqi < 200) {return ["Unhealthy", "#FF0000"];}
    else if (aqi < 300) {return ["Very Unhealthy", "#99004C"];}
    else if (aqi < 500) {return ["Hazardous", "#7E0023"];}
}