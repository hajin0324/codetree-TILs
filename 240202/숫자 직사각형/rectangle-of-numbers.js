const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ").map(Number);
let n = input[0], m = input[1];

let arr = Array(input[0]).fill(0).map(() => Array(input[1]).fill(0));
let cnt = 1;

for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
        arr[i][j] = cnt;
        cnt++;
    }
}

for (let row of arr) {
    let result = "";
    for (let elem of row) {
        result += elem + " ";
    }
    console.log(result);
}