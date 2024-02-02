const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());

let alpha = 'A'.charCodeAt();
for (let i = 0; i < n; i++) {
    let result = "";
    for (let j = 0; j < n; j++) {
        result += String.fromCharCode(alpha);
        alpha += 1
    }
    console.log(result);
}