const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");

for (let e of input) {
    e = e.split(" ");
    console.log(e[0] * e[1]);    
    if (e[2] == 'C') {
        break;
    }
}