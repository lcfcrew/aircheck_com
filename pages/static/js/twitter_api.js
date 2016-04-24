/**
 * Created by kobnar on 4/24/16.
 */

function postSentiment(text, complete) {

    // Convert data to JSON string
    var data = {'text': JSON.stringify(text)};

    // Submit POST request
    $.ajax({
        url: '/api/v1/sentiments/',
        type: 'POST',
        dataType: 'json',
        data: data
    })
        .complete(function (data, status) {
            data.responseText = JSON.parse(data.responseText);
            complete(data, status)
        })
    
}

function updateTweets(complete) {

    // Submit GET request
    $.ajax({
        url: '/api/v1/sentiments/tweets/new/',
        type: 'GET',
        dataType: 'json',
        data: query
    })
        .complete(function (data, status) {
            data.responseText = JSON.parse(data.responseText);
            complete(data, status)
        })

}

function getSentiments(complete) {

    // Submit GET request
    $.ajax({
        url: '/api/v1/sentiments/?analyze=True',
        type: 'GET',
        dataType: 'json',
        data: query
    })
        .complete(function (data, status) {
            data.responseText = JSON.parse(data.responseText);
            complete(data, status)
        })

}
