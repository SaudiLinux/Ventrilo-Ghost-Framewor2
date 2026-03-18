import base64, urllib.parse, random

class GhostAI:
    def __init__(self):
        self.encodings = ["hex", "base64", "double_url", "char_code"]

    def mutate(self, payload):
        """تحوير الحمولة بناءً على استراتيجية عشوائية لتضليل الـ WAF"""
        mode = random.choice(self.encodings)
        if mode == "base64":
            return base64.b64encode(payload.encode()).decode()
        elif mode == "hex":
            return "".join([hex(ord(c)).replace("0x", "%") for c in payload])
        elif mode == "double_url":
            return urllib.parse.quote(urllib.parse.quote(payload))
        elif mode == "char_code":
            codes = [str(ord(c)) for c in payload]
            return f"String.fromCharCode({','.join(codes)})"
        return payload