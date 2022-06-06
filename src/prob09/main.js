// Work on POSIX and Windows
var fs = require("fs");
var stdinBuffer = fs.readFileSync(0); // STDIN_FILENO = 0
var data = stdinBuffer.toString().trim().split(/\s+/);

// 由命令列參數所輸入的資料存放在 data 總體陣列變數

// ========================================================
// 千萬不要修改『上面』的程式碼!
// ========================================================

// 1. 你所寫的程式碼只能在這個段落以下。
// 2. 請依照題目說明完成欠缺的程式碼。


// ========================================================
// 千萬不要修改『下面』的程式碼!
// ========================================================

function main() {
    for(let v of analysis(data))
        process.stdout.write(`${v} `);
    console.log();
}

main()


