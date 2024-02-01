const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");

let count = 0;
for (let i = 0; i < 3; i++) {
    let p = input[i].split(" ");
    if (p[0] == 'Y' && Number(p[1]) >= 37) {
        count += 1;
    }
}

if (count >= 2) {
    console.log("E");
} else {
    console.log("N");
}