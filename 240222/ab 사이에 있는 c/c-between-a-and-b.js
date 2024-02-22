const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ").map(Number);
let a = input[0], b = input[1], c = input[2];
let satisfied = false;

for (let i = a; i <= b; i++) {
    if (i % c == 0) {
        satisfied = true;
        break;
    }
}

if (satisfied) {
    console.log("YES");
} else {
    console.log("NO");
}