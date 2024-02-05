const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n").map(Number);
let cnt = 0;

for (let e of input) {
    if (e % 2 == 0) cnt += 1;
}

console.log(cnt);