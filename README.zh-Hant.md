# PHP-CGI Injector

[English](./README.md) | 繁體中文

🚀 **CVE-2024-4577 & CVE-2024-8926 Exploit Tool**

> 針對 **PHP-CGI 參數注入漏洞** 的自動化測試工具，支援 **CVE-2024-4577** 和 **CVE-2024-8926**，可進行 **命令執行、文件上傳、下載** 等操作。

---

## **📌 介紹**
本工具可用於測試 **PHP-CGI 環境中的參數注入漏洞**，並提供：
- ✅ **自動掃描漏洞**
- ✅ **多種攻擊模式**
- ✅ **支援 `system()` 命令執行**
- ✅ **支援 `eval()`任意程式執行**
- ✅ **支援上傳與下載檔案**
- ✅ **可自動記錄命令執行歷史 (`--log`)**
- ✅ **自動轉換輸出編碼，避免亂碼**

---

## **📜 免責聲明**
**本工具僅限於合法測試與學術用途，請勿用於未經授權的系統！**
> **⚠️ 非法使用將承擔法律責任！**

本工具僅供：
- 🔹 **企業紅隊滲透測試**
- 🔹 **CTF 安全研究**
- 🔹 **個人安全學習**
  
---

## **📥 安裝依賴套件**
使用本工具需安裝依賴套件，請使用以下指令進行安裝。
```bash
pip install -r requirements.txt
```
或者手動安裝：
```bash
pip install requests urllib3 chardet
```

---

## **🛠️ 使用方法**
### **📌 基本用法**
```bash
python exploit.py -u <目標網站> [--timeout=sec] [--log]
```
範例：
```bash
python exploit.py -u http://example.com --timeout=30 --log
```

### **📌 參數選項**
| 參數 | 說明 | 範例 |
|------|------|------|
| `-u` | 指定目標網站 | `-u http://example.com` |
| `--timeout=sec` | 設定請求超時 (`1-120` 秒)，`0` 代表無限等待 | `--timeout=30` |
| `--log` | 啟用 Shell 模式的自動記錄 | `--log` |

---

## **📌 操作模式**
當腳本找到漏洞後，會顯示選單：
```
[+] 找到漏洞入口 : /php-cgi/php-cgi.exe (漏洞編號: CVE-2024-4577)

[*] 現在目標: http://example.com/ (漏洞編號: CVE-2024-4577)
模式選擇:
1) Shell模式 (使用system()執行命令)
2) PHP自訂義模式 (使用eval()執行任意程式)
3) 上傳檔案
4) 下載檔案
5) 切換攻擊目標
6) 離開程式
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
執行 **自訂 PHP 程式**：
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
📂 **檔案下載後儲存於 `download/`，若有重複，會自動增加編號**
```
[*] 已下載至 download/index.php
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
