def get_headers():
    cookie = input("[?] Enter session cookie (optional): ")
    headers = {}

    if cookie:
        headers['Cookie'] = cookie

    return headers
