const fs = require("fs");
let a = Number(fs.readFileSync(0).toString().trim());

if (10 <= a && a <= 20) {
    console.log("yes");
} else {
    console.log("no");
}