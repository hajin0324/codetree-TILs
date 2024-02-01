const fs = require("fs");
let score = fs.readFileSync(0).toString().trim().split(" ");

let mid = Number(score[0]);
let fin = Number(score[1]);

if (mid >= 90 && fin >= 95) {
    console.log(100000);
} else if (mid >= 90 && fin >= 90) {
    console.log(50000);
} else {
    console.log(0);
}