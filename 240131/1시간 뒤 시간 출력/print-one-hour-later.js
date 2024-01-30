const fs = require("fs");
let time = fs.readFileSync(0).toString().split(":");

let h = Number(time[0]);
let m = Number(time[1]);

console.log(h + 1 + ":" + m);