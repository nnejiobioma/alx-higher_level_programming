$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    $('DIV#hello').empty();
    const languageLen = $('INPUT#language_code').val();
    $.ajax({
      method: 'GET',
      url: 'https://fourtonfish.com/hellosalut/?lang=' + languageLen
      success: function (data) {
        $('DIV#hello').append(data.hello);
      }
    });
  });
});
