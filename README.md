# PHP-CGI Injector

🚀 **CVE-2024-4577 & CVE-2024-8926 Exploit Tool**

> 針對 **PHP-CGI 參數注入漏洞** 的自動化測試工具，支持 **CVE-2024-4577** 和 **CVE-2024-8926**，可進行 **命令執行、文件上傳、下載** 等操作。

---

## **📌 介紹**
本工具可用於測試 **PHP-CGI 環境中的參數注入漏洞**，並提供：
- ✅ **超酷的banner動畫**
- ✅ **超酷的終端介面**
- ✅ **自動掃描漏洞**
- ✅ **Tor隱藏攻擊流量**
- ✅ **多種攻擊模式**
- ✅ **預設多種Payload與自訂Payload**
- ✅ **多種Bypass WAF模組**
- ✅ **支持交互式shell**
- ✅ **支持任意php代碼執行**
- ✅ **支持上傳與下載檔案**
- ✅ **可自動記錄命令執行歷史 (`--log`)**
- ✅ **自動轉換輸出編碼**
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
python exploit.py [-h] -u URL [--timeout TIMEOUT] [--log] [--verbose] [--payload [PAYLOAD]] [--tor] [--bypass]
```
範例：
```bash
python exploit.py -u http://example.com --timeout=30 --log --payload --tor --verbose
```

### **📌 參數選項**
| 參數 | 說明 | 範例 |
|------|------|------|
| `-u` 、 `--url` | 指定目標網站 | `-u http://example.com` |
| `--timeout sec` | 設定請求超時 (`1-120` 秒)，`0` 代表無限等待 | `--timeout 30` 、  `--timeout 0` |
| `--log` | 啟用 Shell 模式的自動記錄 | `--log` |
| `--payload`  | 切換或自訂payload組合 | `--payload` 、 `--payload 2` 、 `--payload C` |
| `--tor`  | 使用tor發送請求 | `--tor` |
| `--verbose` | 列出更詳細的測試訊息 | `--verbose` |
| `--bypass` | 進入bypass WAF測試模式 | `--bypass` |
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
6) ❌ 離開程式
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

### **6️⃣ 離開程式**
```
[*] 程式結束
```

---

## 更新日誌
| 版本 | 更新內容 |
|------|------|
| 1.1.2 | 修復命令與任意代碼執行時，編碼問題導致的錯誤。 |
| | 修復執行結果單次儲存默認本地檔案命名的邏輯問題。 |
| 1.2.0 | 修復tor路由連線問題。 |
| | 新增tor自動檢測與連線、Payload自選功能。 |
| 1.3.0 | 新增詳細輸出，用於更好的判斷與調適。 |
| | 新增自訂payload功能。 |
| | 修補Linux上tor連線問題。 |
| 1.3.1 | 修補未找到漏洞時，payload切換的bug |
| 1.4.0 | 新增bypass模式 |
| | 優化exploit.py |
| | 彩蛋動畫 |
| 1.4.1 | 修復不同選單切換時可能導致的錯誤 |
| | 新增超酷終端介面 |
| | 細節優化 |
---

