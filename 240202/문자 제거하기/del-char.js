const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");

let str = input[0];
let arr = input.slice(1).map(Number);

for (let idx of arr) {
    if (str.length <= idx) {
        idx = str.length - 1;
    }

    str = str.slice(0, idx) + str.slice(idx + 1);
    console.log(str);
    
    if (str.length === 1) {
        break;
    }
}