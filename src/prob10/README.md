# 動態網頁設計 (2022 Spring) 期末測驗

### [問題 10]：將隨機輸入的 N 筆資料套用HTML表格樣板輸出。

- 請依照題目說明，在『指定段落』完成欠缺的程式碼。
- 設計 `htmlTable(arr)` 函數，將隨機輸入的 N 筆資料套用HTML表格樣板輸出，請參考簡易測試。
- 為了方便自動檢查輸出結果，請不要加入任何額外的設定，例如字體大小或是CSS樣式設定。
- 輸出格式不需要特別縮排，只要是合法的 HTML 都可通過測試。
- 資料格式： `時間 溫度`
- HTML 表格樣板範例：
    - 輸入資料：`0 210 5 180`
    ```html
    <table>
        <tr>
            <th>時間</th> <th>豆子溫度</th>
        </tr>
        <tr>
            <td>0</td> <td>210</td>
        </tr>
        <tr>
            <td>5</td> <td>180</td>
        </tr>
    </table>
    ````

    `瀏覽器輸出結果：`
    <table>
        <tr>
            <th>時間</th> <th>豆子溫度</th>
        </tr>
        <tr>
            <td>0</td> <td>210</td>
        </tr>
        <tr>
            <td>5</td> <td>180</td>
        </tr>
    </table>


### 簡易測試
```Powershell
prob10> 1,2,3,4 | node .\main.js
<table>
  <tr>
    <th>時間</th> <th>豆子溫度</th>
  </tr>
  <tr>
    <td>1</td> <td>2</td>
  </tr>
  <tr>
    <td>3</td> <td>4</td>
  </tr>
</table>

prob10> 0,220,5,190,10,170,15,140 | node .\main.js
<table>
  <tr>
    <th>時間</th> <th>豆子溫度</th>
  </tr>
  <tr>
    <td>0</td> <td>220</td>
  </tr>
  <tr>
    <td>5</td> <td>190</td>
  </tr>
  <tr>
    <td>10</td> <td>170</td>
  </tr>
  <tr>
    <td>15</td> <td>140</td>
  </tr>
</table>
```

### 自動批閱測試
```Powershell
********************************************
*         Dynamic Web Programming          *
*  Exercises / Homework Automatic Grading  *
********************************************

Test Data : 0 51 5 84 10 54 15 99
Test Data : 0 6 5 54 10 16 15 19 20 2 25 89
Test Data : 0 55 5 9 10 14 15 89 20 66
Test Data : 0 49 5 88 10 96 15 71 20 17 25 1 30 31
Test Data : 0 80 5 85 10 62 15 69 20 100 25 95 30 48
Test Data : 0 10 5 18 10 55 15 53
Test Data : 0 1 5 56 10 71 15 10 20 21 25 78
Test Data : 0 35 5 46 10 88 15 16 20 57 25 65 30 42
Test Data : 0 40 5 60 10 45 15 43 20 66 25 14 30 69 35 99 40 15
Test Data : 0 98 5 19 10 58 15 15

測試通過!

<table>
  <tr>
    <th>時間</th> <th>豆子溫度</th>
  </tr>
  <tr>
    <td>0</td> <td>98</td>
  </tr>
  <tr>
    <td>5</td> <td>19</td>
  </tr>
  <tr>
    <td>10</td> <td>58</td>
  </tr>
  <tr>
    <td>15</td> <td>15</td>
  </tr>
</table>
```

