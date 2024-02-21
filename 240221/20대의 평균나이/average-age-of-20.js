const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n").map(Number);

let idx = 0;
let sum = 0;

while (true) {
    if (parseInt(input[idx] / 10) != 2) {
        break;
    }
    sum += input[idx];
    idx += 1;
}

console.log((sum / idx).toFixed(2));