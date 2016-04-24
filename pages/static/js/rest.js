var bingMapsKey = "AiTVpjhhaRIYHXjnLt1NI8-u83qqwvVqYXsH1EsxB8_yLO8dBQ-pUIPybjZTlyve";

// returns a list of latest 3 tweets
function getSentiments(NumOfSentiments) {
    var sentiments = {
        "sentiments": [{
            "message": "I love breathing so, so much...",
            "lat": 34,
            "long": -118.003
        }, {
            "message": "I love breathing so, so much...",
            "lat": 34,
            "long": -118.003
        }, {
            "message": "I love breathing so, so much...",
            "lat": 34,
            "long": -118.003
        }, ]
    }

    return sentiments;
}

function postSentiment(string) {
    return "id or key of the twitter post and the lat, long so it can orbit there"    ;
}

// Gets a GeoIP as input from server and returns the lat and long
function getLatLongFromGeoIP() {
    return [33.000, -118.000];
}

function getLatLongFromString(query, addMarker, UpdateLatLong) // var is a string like "Los Angeles", gets a location back
{
    var geocodeRequest = "http://dev.virtualearth.net/REST/v1/Locations?query=" + encodeURIComponent(query) + "&key=" + bingMapsKey;
    CallRestService(geocodeRequest, UpdateLatLong);
    var topResult;

}



//// CHRIS VIA DJANGO BACKEND
//function getAirAnalysis(query) {
//
// getLatLongFromString(query, addMarker)
////    return "somedata";
//}

function CallRestService(request, callback) {
    $.ajax({
        url: request,
        dataType: "jsonp",
        jsonp: "jsonp",
        success: function (r) {
            callback(r);
        },
        error: function (e) {
            alert("Error" + e.statusText);
        }
    });
}