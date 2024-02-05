const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n").map(Number);
let cnt3 = 0, cnt5 = 0;

for (let e of input) {
    if (e % 3 == 0) cnt3 += 1;
    if (e % 5 == 0) cnt5 += 1;
}

console.log(cnt3, cnt5);