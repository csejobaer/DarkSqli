import requests

def scan_api(endpoint):
    try:
        r = requests.get(endpoint)
        return {
            "endpoint": endpoint,
            "status": r.status_code
        }
    except:
        return {
            "endpoint": endpoint,
            "status": "error"
        }
