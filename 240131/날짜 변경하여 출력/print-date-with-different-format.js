const fs = require("fs");
let date = fs.readFileSync(0).toString().split(".");

let y = Number(date[0]);
let m = Number(date[1]);
let d = Number(date[2]);

console.log(`${m}-${d}-${y}`);