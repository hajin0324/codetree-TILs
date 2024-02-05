const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ").map(Number);
let sumVal = 0;

for (let i = input[0]; i <= input[1]; i++) {
    sumVal += i;
}

console.log(sumVal);