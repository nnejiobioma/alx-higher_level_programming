const $headerElement = $('header');
const $divHeader = $('DIV#toggle_header');

$divHeader.on('click', () => {
  const currentClass = $headerElement.attr('class');

  if (currentClass === 'green') {
    $headerElement.toggleClass(`${currentClass} red`);
  }

  if (currentClass === 'red') {
    $headerElement.toggleClass(`${currentClass} green`);
  }
});
