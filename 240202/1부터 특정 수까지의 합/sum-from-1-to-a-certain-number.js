function sumN(n) {
    let sumVal = 0;
    for (let i = 1; i <= n; i++) {
        sumVal += i;
    }

    return sumVal / 10;
}

const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());

console.log(sumN(n));