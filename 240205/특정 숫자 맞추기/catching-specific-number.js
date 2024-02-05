const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");

for (let e of input) {
    if (e < 25) {
        console.log("Higher");
    } else if (e > 25) {
        console.log("Lower");
    } else {
        console.log("Good");
        break;
    }
}