const $headerElement = $('header');
const $divHeader = $('div#red_header');

$divHeader.on('click', function () {
  $headerElement.addClass('red');
});
