const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");
let cnt = 0;

for (let e of input) {
    if (e % 2 == 0) {
        console.log(parseInt(e / 2));
        cnt += 1;
    }

    if (cnt == 3) {
        break;
    }

}