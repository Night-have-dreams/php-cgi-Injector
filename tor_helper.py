import platform
import time
import subprocess
import os
import requests

try:
    from requests_tor import RequestsTor
except ImportError:
    print("[!] 警告：請安裝 `requests-tor` 以支援 Tor 代理: pip install requests-tor")
    RequestsTor = None

# 偵測作業系統
IS_WINDOWS = platform.system().lower() == "windows"

# 設定 Tor 代理端口
TOR_PORT = 9150 if IS_WINDOWS else 9050

# 直接設定 Proxies（用於 Windows）
PROXIES = {
    "http": f"socks5h://127.0.0.1:{TOR_PORT}",
    "https": f"socks5h://127.0.0.1:{TOR_PORT}"
}

def check_tor():
    """檢查 Tor 代理是否可用，回傳 RequestsTor 會話或 False"""
    if not RequestsTor:
        return False
    try:
        # 先用 requests 測試，確保 Tor 瀏覽器的 SOCKS 代理可用
        response = requests.get("https://check.torproject.org/api/ip", proxies=PROXIES, timeout=10)
        if response.status_code == 200:
            ip_check = response.json().get("IP", "未知")
            print(f"[*] Tor 代理已啟用，當前出口 IP: {ip_check}")
            return RequestsTor()  # 改成不帶參數，讓 requests-tor 自動偵測代理
    except Exception as e:
        print(f"[!] 無法連接 Tor 代理: {e}")
        return False
    return False

def start_tor():
    """自動啟動 Tor（Windows: Tor 瀏覽器，Linux/macOS: Tor 服務）"""
    if IS_WINDOWS:
        print("[*] 嘗試開啟 Tor 瀏覽器...")
        possible_paths = [
            os.path.expandvars(r"%APPDATA%\Tor Browser\Browser\firefox.exe"),
            r"C:\Program Files\Tor Browser\Browser\firefox.exe",
            r"D:\Tor Browser\Browser\firefox.exe",
            os.path.expandvars(r"%USERPROFILE%\Desktop\Tor Browser\Browser\firefox.exe"),
            r"C:\Users\Public\Desktop\Tor Browser\Browser\firefox.exe"
        ]
        tor_path = next((path for path in possible_paths if os.path.exists(path)), None)
        
        if not tor_path:
            print("[!] 找不到 Tor 瀏覽器，請手動開啟 Tor！")
            return False
        subprocess.Popen(tor_path, shell=True)
    else:
        print("[*] 嘗試啟動 Tor 服務...")
        subprocess.Popen("tor &", shell=True)
    
    print("[*] 等待 Tor 啟動中...")
    time.sleep(10)  # 等待 Tor 啟動
    return check_tor()

def get_tor_session():
    """回傳 RequestsTor 會話，如果不可用則詢問是否啟動 Tor"""
    print("[*] 嘗試啟動 Tor 代理...")
    print("[*] Tor 代理回應時間較長，建議設定 --timeout")

    tor_session = check_tor()
    if not tor_session:
        if IS_WINDOWS:
            print("[!] 錯誤：無法連接 Tor 代理，請確認 Tor 瀏覽器是否開啟！")
            print("[*] 請確保 Tor 瀏覽器已開啟，並且 `SOCKS 代理` 設定為 `127.0.0.1:9150`")
        else:
            print("[!] 錯誤：無法連接 Tor 代理，請確認 Tor 服務是否運行！")
            print("[*] Linux 用戶請嘗試執行: `sudo systemctl start tor`")
        
        user_input = input("[?] 是否要自動開啟 Tor？ (Y/N): ").strip().lower()
        if user_input == "y":
            tor_session = start_tor()
            if tor_session:
                print("[*] Tor 成功啟動！")
            else:
                print("[!] Tor 啟動失敗，請手動開啟！")
                return None
        else:
            print("[!] Tor 未啟動，無法使用 --tor 模式！")
            return None
    return tor_session
