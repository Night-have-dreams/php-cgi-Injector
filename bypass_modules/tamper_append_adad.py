# tamper_append_adad.py

import random
import string

name = "tamper_append_adad"
description = "在 payload 結尾添加 %AD%AD+隨機字串，增加混淆與變異性"

def generate_random_suffix(length=12):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def tamper(data):
    payload = data.get("payload", "")
    suffix = generate_random_suffix()
    payload += f"+%AD%AD+{suffix}"
    data["payload"] = payload
    return data
