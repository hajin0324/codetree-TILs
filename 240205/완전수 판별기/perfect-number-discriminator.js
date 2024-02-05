const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());
let sumVal = 0;

for (let i = 1; i < n; i++) {
    if (n % i == 0) sumVal += i;
}

if (n == sumVal) console.log("P");
else console.log("N");