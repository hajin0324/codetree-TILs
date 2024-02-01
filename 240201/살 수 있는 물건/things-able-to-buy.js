const fs = require("fs");
let money = Number(fs.readFileSync(0).toString().trim());

if (money >= 3000) {
    console.log("book");
} else {
    console.log("mask");
}