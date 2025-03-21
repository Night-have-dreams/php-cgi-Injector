# tamper_cgi_case_mixer.py

import random
import os

name = "tamper_cgi_case_mixer"
description = "混淆php執行檔名的大小寫"

def tamper(data):
    cgipoint = data.get("cgipoint", "")
    if not cgipoint:
        return data

    # 分離目錄與檔案名稱
    dir_name, file_name = os.path.split(cgipoint)
    
    # 對檔案名稱部分進行大小寫混合
    mixed_file_name = ''.join(
        [char.upper() if random.random() < 0.5 else char.lower() for char in file_name]
    )

    # 重新組合完整的CGI路徑
    mixed_cgipoint = os.path.join(dir_name, mixed_file_name).replace('\\', '/')

    # 更新請求資料
    data["cgipoint"] = mixed_cgipoint

    return data
