def generate_exploit(vulnerability_type):
    if vulnerability_type == "SQLi":
        return "Payload: ' OR 1=1 --"
    elif vulnerability_type == "XSS":
        return "<script>alert('XSS')</script>"
    elif vulnerability_type == "LFI":
        return "../../etc/passwd"
    else:
        return "No exploit available."

print(generate_exploit("SQLi"))
