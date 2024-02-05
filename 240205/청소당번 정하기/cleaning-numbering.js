const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());
let day2 = 0, day3 = 0, day12 = 0;

for (let i = 1; i <= n; i++) {
    if (i % 12 == 0) {
        day12 += 1;
    } else if (i % 3 == 0) {
        day3 += 1;
    } else if (i % 2 == 0) {
        day2 += 1;
    }
}

console.log(day2, day3, day12);