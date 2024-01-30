const fs = require("fs");
let input = fs.readFileSync(0).toString().split("\n");

let c = input[0].trim();
let a = Number(input[1]).toFixed(2);
let b = Number(input[2]).toFixed(2);

console.log(c);
console.log(a);
console.log(b);