#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (Number.isNaN(size)) {
	console.log('Missing size');
} else {
	for(let i = 0, s; i < size; i++) {
		s = '';
		for( let h = 0; h < size; h++) {
			s += 'X';
		}
		console.log(s);
	}
}
