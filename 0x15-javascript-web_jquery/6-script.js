const $updateHeader = $('div#update_header');
const $headerElement = $('header');

$updateHeader.on('click', () => {
  $headerElement.text('New Header!!!');
});
