const fs = require("fs");
let sight = Number(fs.readFileSync(0).toString().trim());

if (sight >= 1.0) {
    console.log("High");
} else if (sight >= 0.5) {
    console.log("Middle")
} else {
    console.log("Low");
}