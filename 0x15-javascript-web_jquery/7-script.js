$(document).ready(function () {
    $.ajax({
        // url for the request
        url: "https://swapi-api.hbtn.io/api/people/5/?format=json",
        method: "GET",
        datatype: "json",
    })
    .done(function( json ) {
        $("DIV#character").text( json.name );
    })
});
