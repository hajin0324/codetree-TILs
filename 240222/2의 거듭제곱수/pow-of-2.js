const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());
let cnt = 1, x = 1;

while (true) {
    if ((2 ** x) == n) {
        console.log(cnt);
        break;
    } 
    x++;
    cnt++;
}