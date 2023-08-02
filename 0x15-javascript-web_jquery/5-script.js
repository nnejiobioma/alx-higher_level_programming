const $listElement = $('ul.my_list');
const $addItem = $('div#add_item');

$addItem.on('click', () => {
  $listElement.append('<li>Item</li>');
});
