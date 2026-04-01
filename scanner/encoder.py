import urllib.parse

def encode_payload(payload):
    # basic URL encoding
    return urllib.parse.quote(payload)
