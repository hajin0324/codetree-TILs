const fs = require("fs");
let input = fs.readFileSync(0).toString().split(" ");

let w = Number(input[0]);
let l = Number(input[1]);

w += 8;
l *= 3;

console.log(w);
console.log(l);
console.log(w * l);