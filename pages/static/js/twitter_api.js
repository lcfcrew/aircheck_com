/**
 * Created by kobnar on 4/24/16.
 */

function postSentiment(complete) {
 var text = document.getElementById('input_message').value;

    // Convert data to JSON string
    var dataPost = JSON.stringify({'text': text});
//    alert(dataPost);

    // Submit POST request
    $.ajax({
        url: '/api/v1/sentiments/',
        type: 'POST',
        dataType: 'json',
        data: dataPost
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
