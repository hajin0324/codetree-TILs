const fs = require("fs");
let score = fs.readFileSync(0).toString().trim().split("\n");

let a = score[0].split(" ");
let b = score[1].split(" ");

let aMath = Number(a[0]), aEng = Number(a[1]);
let bMath = Number(b[0]), bEng = Number(b[1]);

if (aMath > bMath) {
    console.log("A");
} else if(bMath > aMath) {
    console.log("B");
} else {
    console.log(aEng > bEng ? "A" : "B");
}