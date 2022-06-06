# 動態網頁設計 (2022 Spring) 期末測驗

### [問題 2]：設計一函數加總 `3` 個隨機數字。

- 請依照題目說明，在『指定段落』完成欠缺的程式碼。
- 設計一個 `add(x, y, z)` 函數，加總用『管線(pipe) `|`』輸入的 `3` 個隨機數字，請參考簡易測試。
- 參考 Week 13 作業 `hw02`：『數字/文字(Number/Text)傻傻分不清楚。』
- 建議使用 JavaScript `Number(...)` 函數將參數轉成數字型態。

### 簡易測試
```Powershell
prob02> 1,2,3 | node .\main.js
6

prob02> 11,22,33 | node .\main.js
66

prob02> 5,6,7 | node .\main.js   
18
```

### 自動批閱測試
```Powershell
prob02> .\test.ps1

********************************************
*         Dynamic Web Programming          *
*  Exercises / Homework Automatic Grading  *
********************************************

Test Data : 47 66 36
Test Data : 25 30 30
Test Data : 52 93 20
Test Data : 77 98 47
Test Data : 58 8 67
Test Data : 47 45 56
Test Data : 26 10 8
Test Data : 61 9 67
Test Data : 54 61 35
Test Data : 72 100 70

測試通過!

242
```

