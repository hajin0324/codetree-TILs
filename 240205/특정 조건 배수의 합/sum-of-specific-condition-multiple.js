const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ").map(Number);
let sumVal = 0;

if (input[0] > input[1]) input = [input[1], input[0]];
for (let i = input[0]; i <= input[1]; i++) {
    if (i % 5 == 0) sumVal += i;
}

console.log(sumVal);