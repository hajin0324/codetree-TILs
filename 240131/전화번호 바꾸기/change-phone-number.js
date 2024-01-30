const fs = require("fs");
let phone = fs.readFileSync(0).toString().split("-");

let s = Number(phone[1]);
let t = Number(phone[2]);

[s, t] = [t, s];

console.log(`010-${s}-${t}`);