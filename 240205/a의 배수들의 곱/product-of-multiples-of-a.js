const fs = require("fs");
let n = fs.readFileSync(0).toString().trim().split(" ").map(Number);
let prod = 1;

for (let i = 1; i <= n[1]; i++) {
    if (i % n[0] == 0) prod *= i;
}

console.log(prod);