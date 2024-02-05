const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ").map(Number);
let prod = 1;

for (let i = 1; i <= input[1]; i++) {
    prod *= input[0];
}

console.log(prod)