const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n").map(Number);
let sumVal = 0;

for (let e of input.slice(1)) {
    sumVal += e;
}


console.log(sumVal, (sumVal / input[0]).toFixed(1));