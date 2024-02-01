const fs = require("fs");
let input = fs.readFileSync(0).toString().split(" ");

let height = Number(input[0]);
let weight = Number(input[1]);

let bmi = (weight * 10000) / (height ** 2);
console.log(parseInt(bmi));

if (bmi >= 25) {
    console.log("Obesity");
}