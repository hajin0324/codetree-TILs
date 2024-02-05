const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");

input.slice(1).forEach(e => {
    if (e % 2 != 0 && e % 3 == 0) {
        console.log(e);
    }
})