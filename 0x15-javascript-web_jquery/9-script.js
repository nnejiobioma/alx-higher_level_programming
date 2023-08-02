$(document).ready(function () {
    $.ajax({
        url: "https://fourtonfish.com/hellosalut/?lang=fr",
        method: "GET",
        datatype: "json",
    })
    .done(function( json ){
        $("DIV#hello").text(json.hello);
    })
});
