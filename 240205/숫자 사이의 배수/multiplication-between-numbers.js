const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ").map(Number);
let cnt = 0, sumVal = 0;

for (let i = input[0]; i <= input[1]; i++) {
    if (i % 5 == 0 || i % 7 == 0) {
        cnt += 1;
        sumVal += i;
    }
}

console.log(sumVal, (sumVal / cnt).toFixed(1));