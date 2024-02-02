function divideEven(arr) {
    let result ="";
    for (let e of arr) {
        if (e % 2 == 0) {
            e /= 2;
        }
        result += e + " ";
    }
    console.log(result);
}

const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");

let n = Number(input[0]);
let arr = input[1].split(" ").map(Number);

divideEven(arr);