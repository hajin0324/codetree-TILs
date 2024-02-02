const fs = require("fs");
let arr = fs.readFileSync(0).toString().trim().split(" ").map(Number);

let sum = 0
for (let elem of arr) {
    sum += elem;
}

console.log(sum);