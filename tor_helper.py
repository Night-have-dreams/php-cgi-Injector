import platform
import time
import subprocess
import os
import requests
from rich import print as rprint
from rich.panel import Panel
from rich.console import Console
from rich.text import Text
from rich.markdown import Markdown
from rich.syntax import Syntax
from rich.table import Table

try:
    from requests_tor import RequestsTor
except ImportError:
    rprint("[bold dark_violet][!] 警告：請安裝 `requests-tor` 以支援 Tor 代理: pip install requests-tor[/bold dark_violet]")
    RequestsTor = None

IS_WINDOWS = platform.system().lower() == "windows"
TOR_PORT = 9150 if IS_WINDOWS else 9050

PROXIES = {
    "http": f"socks5h://127.0.0.1:{TOR_PORT}",
    "https": f"socks5h://127.0.0.1:{TOR_PORT}"
}

def check_tor():
    if not RequestsTor:
        return False
    try:
        response = requests.get("https://check.torproject.org/api/ip", proxies=PROXIES, timeout=10)
        if response.status_code == 200:
            ip_check = response.json().get("IP", "未知")
            rprint(f"[medium_purple][*] Tor 代理已啟用，當前出口 IP: {ip_check}[/medium_purple]")
            if IS_WINDOWS:
                return RequestsTor()
            else:
                return RequestsTor(tor_ports=(9050,))
    except Exception as e:
        rprint(f"[bold dark_violet][!] 無法連接 Tor 代理: {e}[/bold dark_violet]")
        return False
    return False

def start_tor():
    if IS_WINDOWS:
        rprint("[orchid][*] 嘗試開啟 Tor 瀏覽器...[/orchid]")
        possible_paths = [
            os.path.expandvars(r"%APPDATA%\Tor Browser\Browser\firefox.exe"),
            r"C:\Program Files\Tor Browser\Browser\firefox.exe",
            r"D:\Tor Browser\Browser\firefox.exe",
            os.path.expandvars(r"%USERPROFILE%\Desktop\Tor Browser\Browser\firefox.exe"),
            r"C:\Users\Public\Desktop\Tor Browser\Browser\firefox.exe"
        ]
        tor_path = next((path for path in possible_paths if os.path.exists(path)), None)

        if not tor_path:
            rprint("[bold dark_violet][!] 找不到 Tor 瀏覽器，請手動開啟 Tor！[/bold dark_violet]")
            return False
        subprocess.Popen(tor_path, shell=True)
    else:
        rprint("[orchid][*] 嘗試啟動 Tor 服務...[/orchid]")
        subprocess.Popen("tor &", shell=True)

    rprint("[orchid][*] 等待 Tor 啟動中...[/orchid]")
    time.sleep(10)
    return check_tor()

def get_tor_session():
    rprint("[medium_purple][*] 嘗試啟動 Tor 代理...[/medium_purple]")
    rprint("[dim][!] Tor 代理回應時間較長，建議設定 --timeout[/dim]")

    tor_session = check_tor()
    if not tor_session:
        if IS_WINDOWS:
            rprint("[bold dark_violet][!] 無法連接 Tor 代理，請確認 Tor 瀏覽器是否開啟！[/bold dark_violet]")
            rprint("[orchid][*] 請確保 Tor 瀏覽器已開啟，並且 SOCKS 代理 設定為 127.0.0.1:9150[/orchid]")
        else:
            rprint("[bold dark_violet][!] 無法連接 Tor 代理，請確認 Tor 服務是否運行！[/bold dark_violet]")
            rprint("[orchid][*] Linux 用戶請嘗試執行: sudo systemctl start tor[/orchid]")

        user_input = input("[?] 是否要自動開啟 Tor？ (Y/N): ").strip().lower()
        print()
        if user_input == "y":
            tor_session = start_tor()
            if tor_session:
                rprint("[bold orchid][+] Tor 成功啟動！[/bold orchid]\n")
            else:
                rprint("[bold dark_violet][!] Tor 啟動失敗，請手動開啟！[/bold dark_violet]\n")
                return None
        else:
            rprint("[bold red][!] Tor 未啟動，無法使用 --tor 模式！[/bold red]")
            return None
    return tor_session