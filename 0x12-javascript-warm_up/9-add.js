#!/usr/bin/node
function add (a, b) {
	console.log(paseInt(a) + parseInt(b));
}

add(process.argv[2], process.argv[3]);
