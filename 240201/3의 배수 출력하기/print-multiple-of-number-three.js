const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());

let i = 1;
let result = "";
while (i <= n) {
    if (i % 3 == 0) {
        result += i + " ";
    }
    i += 1
}

console.log(result);