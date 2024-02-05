const fs = require("fs");
let n = fs.readFileSync(0).toString().trim().split(" ").map(Number);
let prod = 1;

for (let i = n[0]; i <= n[1]; i++) {
    prod *= i;
}

console.log(prod);