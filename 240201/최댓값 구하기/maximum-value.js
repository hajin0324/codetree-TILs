const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ");

let a = Number(input[0]);
let b = Number(input[1]);
let c = Number(input[2]);

if (a > b) {
    console.log(a > c ? a : c);
} else {
    console.log(b > c ? b : c);
}