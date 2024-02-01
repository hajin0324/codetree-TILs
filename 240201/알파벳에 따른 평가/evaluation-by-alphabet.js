const fs = require("fs");
let alpha = fs.readFileSync(0).toString().trim();

if (alpha === 'S') {
    console.log("Superior");
} else if (alpha === 'A') {
    console.log("Excellent");
} else if (alpha === 'B') {
    console.log("Good");
} else if (alpha === 'C') {
    console.log("Usually");
} else if (alpha === 'D') {
    console.log("Effort");
} else {
    console.log("Failure");
}