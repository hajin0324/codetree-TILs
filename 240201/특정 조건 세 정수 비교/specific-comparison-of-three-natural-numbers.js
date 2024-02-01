const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ");

let a = Number(input[0]);
let b = Number(input[1]);
let c = Number(input[2]);

let result1 = (a <= b && a <= c) ? 1 : 0;
let result2 = (a == b && a == c) ? 1 : 0;

console.log(result1, result2);