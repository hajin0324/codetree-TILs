const fs = require("fs");
let str = fs.readFileSync(0).toString().trim();

str += 'Hello';
console.log(str);