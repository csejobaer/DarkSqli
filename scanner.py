import requests
from payloads import SQLI_PAYLOADS
from ai_model import predict

def scan(url):
    results = []

    try:
        base = requests.get(url, timeout=5).text
    except:
        return results

    for payload in SQLI_PAYLOADS:
        try:
            r = requests.get(url + payload, timeout=5)

            risk = predict(r.text, base)

            if risk in ["HIGH", "MEDIUM"]:
                results.append({
                    "url": url,
                    "payload": payload,
                    "risk": risk
                })

        except:
            continue

    return results
