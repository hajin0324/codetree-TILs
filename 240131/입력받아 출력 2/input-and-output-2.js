const fs = require("fs");
let input = fs.readFileSync(0).toString().split("-");

let f = Number(input[0]);
let b = Number(input[1]);

console.log(`${f}${b}`);