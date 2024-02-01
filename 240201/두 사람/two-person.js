const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");

let a = input[0].split(" ");
let b = input[1].split(" ");

let aAge = Number(a[0]), aGen = a[1];
let bAge = Number(b[0]), bGen = b[1];

if (aAge >= 19 && aGen === 'M' || bAge >= 19 && bGen === 'M') {
    console.log(1);
} else {
    console.log(0);
}