$(document).ready(function () {
  function translate () {
    $('DIV#hello').empty();
    const languageLen = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://fourtonfish.com/hellosalut/?lang=' + languageLen,
      success: function (data) {
        $('DIV#hello').append(data.hello);
      }
    });
  }
  $('INPUT#btn_translate').click(function () {
    translate();
  });
  $('INPUT#language_code').keypress(function (e) {
    const languageKey = e.which;
    if (languageKey === 13) {
      translate();
    }
  });
});
