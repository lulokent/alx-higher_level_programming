#!/usr/bin/node
function add(a,b){
	const s = a +b;
	console.log(s);
}

add(Number(process.argv[2]), Number(process.argv[3]));
