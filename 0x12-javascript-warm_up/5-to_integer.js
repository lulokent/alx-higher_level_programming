#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined){
	console.log('Not a number');
} else {
	comsole.log('My number:', parseInt(process.argv[2]));
}
