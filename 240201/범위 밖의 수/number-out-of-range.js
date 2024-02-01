const fs = require("fs");
let a = fs.readFileSync(0).toString().trim();

console.log((a < 10 || a > 20) ? "yes" : "no");