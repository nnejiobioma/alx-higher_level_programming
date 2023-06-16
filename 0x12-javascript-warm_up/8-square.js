#!/user/bin/node

const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  const square = 'X'.repeat(size);
  for (let i = 0; i < size; i++) {
    console.log(square);
  }
}
