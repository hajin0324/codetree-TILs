const fs = require("fs");
let m = Number(fs.readFileSync(0).toString().trim());

if (m === 12 || m <= 2) {
    console.log("Winter");
} else if (m <= 5) {
    console.log("Spring");
} else if (m <= 8) {
    console.log("Fall");
}