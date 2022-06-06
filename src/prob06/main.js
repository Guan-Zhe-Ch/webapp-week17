// Work on POSIX and Windows
var fs = require("fs");
var stdinBuffer = fs.readFileSync(0); // STDIN_FILENO = 0
var data = stdinBuffer.toString().trim().split(/\s+/);

// 由命令列參數所輸入的資料存放在 data 總體陣列變數


function apply(dat, filter) {
    arr = []
    for (let v of dat)
        if (filter(v))
            arr.push(v);
    return arr;
}

function gt10(v) {
    return Number(v)>10;
}

// ========================================================
// 千萬不要修改『上面』的程式碼!
// ========================================================


// 1. 你所寫的程式碼只能在這個段落。
// 2. 請依照題目說明完成欠缺的程式碼。


// ========================================================
// 千萬不要修改『下面』的程式碼!
// ========================================================

function main() {
    console.log(`gt10(v) => ${apply(data,gt10)}`);
    console.log(`even(v) => ${apply(data,even)}`);
    console.log(`odd(v)  => ${apply(data,odd)}`);
}


main()


