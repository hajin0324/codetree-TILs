const fs = require("fs");
let ft = Number(fs.readFileSync(0).toString());
let result = ft * 30.48;

console.log(result.toFixed(1));