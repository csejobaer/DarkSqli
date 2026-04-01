import requests
from payloads import SQLI_PAYLOADS, ERRORS

def scan(url):
    results = []

    for payload in SQLI_PAYLOADS:
        test_url = url + payload

        try:
            r = requests.get(test_url, timeout=5)

            for err in ERRORS:
                if err in r.text.lower():
                    results.append({
                        "url": url,
                        "payload": payload,
                        "risk": "Possible SQL Injection"
                    })
                    break

        except:
            continue

    return results
