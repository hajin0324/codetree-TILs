const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ");
let a = Number(input[0]), b = Number(input[1]);
let result = "";

while (a <= b) {
    result += a + " ";
    if (a % 2 == 0) a += 3;
    else a *= 2;
}

console.log(result);