const fs = require("fs");
let date = fs.readFileSync(0).toString().split("-");

let m = Number(date[0]);
let d = Number(date[1]);
let y = Number(date[2]);

console.log(`${y}.${m}.${d}`);