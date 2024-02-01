const fs = require("fs");
let m = Number(fs.readFileSync(0).toString().trim());

if (m == 2) {
    console.log(28);
} else if (m <= 7 && m % 2 != 0 || m >= 8 && m % 2 == 0) {
    console.log(31);
} else {
    console.log(30);
}