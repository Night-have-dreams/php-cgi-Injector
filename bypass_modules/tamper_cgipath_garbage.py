# tamper_cgipath_garbage.py

name = "tamper_cgipath_garbage"
description = "在 CGI 路徑後添加 /%81%F5%81%F5/"

def tamper(data):
    if data.get("cgipoint") and not data["cgipoint"].endswith("/%81%F5%81%F5/"):
        if data["cgipoint"].endswith("/"):
            data["cgipoint"] += "%81%F5%81%F5/"
        else:
            data["cgipoint"] += "/%81%F5%81%F5/"
    return data
