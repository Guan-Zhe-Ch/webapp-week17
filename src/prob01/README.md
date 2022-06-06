# 動態網頁設計 (2022 Spring) 期末測驗

### [問題 1]：使用 `console.log(...)` 和南臺科技大學 Say Hello N次。

- 請依照題目說明，在『指定段落』完成欠缺的程式碼。
- `N` 在PowerShell執行時，用『管線(pipe) `|`』的方式給資料，請參考簡易測試。

### 簡易測試
```Powershell
prob01> 2 | node .\main.js
Hello STUST!
Hello STUST!

prob01> 5 | node .\main.js
Hello STUST!
Hello STUST!
Hello STUST!
Hello STUST!
Hello STUST!

prob01> 1 | node .\main.js
Hello STUST!
```

### 自動批閱測試
```Powershell
prob01> .\test.ps1

********************************************
*         Dynamic Web Programming          *
*  Exercises / Homework Automatic Grading  *
********************************************

Test Data : 4
Test Data : 4
Test Data : 9
Test Data : 1
Test Data : 5
Test Data : 10
Test Data : 10
Test Data : 2
Test Data : 5
Test Data : 7

測試通過!

Hello STUST!
Hello STUST!
Hello STUST!
Hello STUST!
Hello STUST!
Hello STUST!
Hello STUST!
```

