const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n").map(Number);
let cnt = 0, sumVal = 0;

for (let e of input) {
    if ( 0 <= e && e <= 200) {
        sumVal += e;
        cnt += 1
    }
}

console.log(sumVal, (sumVal / cnt).toFixed(1));