import os
import importlib.util
from rich import print as rprint

# 模組所在資料夾
TAMPER_DIR = os.path.join(os.path.dirname(__file__), "bypass_modules")

def load_all_tampers():
    """
    掃描 bypass_modules 中所有 tamper，回傳 dict：模組名稱 -> 描述
    """
    tamper_info = {}

    for filename in os.listdir(TAMPER_DIR):
        if filename.endswith(".py") and not filename.startswith("__"):
            mod_name = filename[:-3]
            mod_path = os.path.join(TAMPER_DIR, filename)

            spec = importlib.util.spec_from_file_location(mod_name, mod_path)
            mod = importlib.util.module_from_spec(spec)
            try:
                spec.loader.exec_module(mod)
                # 確保有 name 與 description 屬性
                if hasattr(mod, "name") and hasattr(mod, "description"):
                    tamper_info[mod.name] = mod.description
                else:
                    rprint(f"[bold red][!] 模組 {filename} 缺少必要資訊，將略過[/bold red]")
            except Exception as e:
                rprint(f"[bold red][!] 載入 {filename} 失敗: {e}[/bold red]")

    return tamper_info


def load_tamper_functions(selected_names):
    """
    根據使用者選定的模組名稱（不是檔名），回傳 tamper 函式清單
    """
    tamper_funcs = []

    for filename in os.listdir(TAMPER_DIR):
        if filename.endswith(".py") and not filename.startswith("__"):
            mod_path = os.path.join(TAMPER_DIR, filename)

            spec = importlib.util.spec_from_file_location(filename[:-3], mod_path)
            mod = importlib.util.module_from_spec(spec)

            try:
                spec.loader.exec_module(mod)
                if hasattr(mod, "name") and mod.name in selected_names and hasattr(mod, "tamper"):
                    tamper_funcs.append(mod.tamper)
            except Exception as e:
                rprint(f"[bold red][!] 載入 tamper 函式失敗: {filename} - {e}[/bold red]")

    return tamper_funcs
