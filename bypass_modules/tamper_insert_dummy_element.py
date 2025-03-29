# tamper_insert_dummy_element.py
import random
import string
import re

name = "tamper_insert_dummy_element"
description = "從 payload 中插入干擾的假參數"

def generate_fake_element():
    key = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{key}%3d1"

def extract_prefix(payload):
    match = re.search(r'(%[a-zA-Z0-9%-]+)\+', payload)
    return match.group(1) if match else "%ADd"

def split_payload(payload, prefix):
    parts = payload.split("+")
    chunks = []
    i = 0
    while i < len(parts) - 1:
        if parts[i] == prefix:
            chunks.append(f"{parts[i]}+{parts[i+1]}")
            i += 2
        else:
            i += 1
    return chunks

def tamper(data):
    payload = data.get("payload", "")
    if not payload:
        return data

    prefix = extract_prefix(payload)
    chunks = split_payload(payload, prefix)

    if not chunks:
        return data

    fake_param = f"{prefix}+{generate_fake_element()}"
    insert_index = random.randrange(0, len(chunks) + 1)

    new_chunks = chunks.copy()
    new_chunks.insert(insert_index, fake_param)

    data["payload"] = "+".join(new_chunks)
    print(f"[{name}] 使用 prefix: {prefix}")
    print(f"[{name}] payload 改為：{data['payload']}")
    return data