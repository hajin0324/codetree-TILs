const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ");

let b = Number(input[0]);
let a = Number(input[1]);

let i = b;
let result = "";

while (i >= a) {
    result += i + " ";
    i--;
}

console.log(result);