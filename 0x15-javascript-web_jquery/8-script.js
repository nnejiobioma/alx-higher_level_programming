$(document).ready(function () {
    $.ajax({
        url: "https://swapi-api.hbtn.io/api/films/?format=json",
        method: "GET",
        datatype: "json",
    })
    .done(function( json ){
        data = json.results;
        for (let x = 0; x < data.length; x++) {
            $("UL#list_movies").append("<li>" + data[x].title + "</li>");
        }
    })
});
