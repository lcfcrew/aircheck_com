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

function UpdateLatLong(data)
{
alert(data);
}

function getLatLongFromString(query) // var is a string like "Los Angeles", gets a location back
{
    var api_url = "http://dev.virtualearth.net/REST/v1/Locations?q=" + query + "&o=json&key=" + bingMapsKey;

     $.ajax({
        url: api_url + query,
        type: "GET",
        success: function(result){
        UpdateLatLong(data);
    }});

//
//    $.ajax({
//        url: api_url + query,
//        data: data,
//
//        dataType: "JSON"})
//            .complete()
}

// CHRIS VIA DJANGO BACKEND
function getAirAnalysis(lat, long) {
    return "somedata";
}