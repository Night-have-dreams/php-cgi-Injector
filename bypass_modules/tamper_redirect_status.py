# tamper_redirect_status.py

name = "tamper_redirect_status"
description = "在請求表頭中添加 Redirect-status: 1，以繞過 CGI 環境驗證"

def tamper(data):
    headers = data.get("headers", {})
    if not isinstance(headers, dict):
        headers = {}

    headers["Redirect-status"] = "1"
    data["headers"] = headers

    return data
