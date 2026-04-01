import re

SQL_ERROR_PATTERNS = [
    r"sql syntax",
    r"mysql_fetch",
    r"ORA-\d+",
    r"SQLite error",
    r"syntax error",
    r"unterminated query",
    r"warning.*mysql",
]

def detect_sql_error(text):
    for pattern in SQL_ERROR_PATTERNS:
        if re.search(pattern, text.lower()):
            return True
    return False


def detect_boolean_diff(baseline, injected):
    return len(baseline) != len(injected)


def detect_time_delay(response_time, threshold=2.5):
    return response_time > threshold


def classify_vulnerability(error, boolean, time):
    if error:
        return "Error-Based SQLi"
    elif time:
        return "Time-Based SQLi"
    elif boolean:
        return "Boolean-Based SQLi"
    return None


def analyze(payload, response_text, baseline, response_time):
    error = detect_sql_error(response_text)
    boolean = detect_boolean_diff(baseline, response_text)
    time = detect_time_delay(response_time)

    vuln_type = classify_vulnerability(error, boolean, time)

    return {
        "payload": payload,
        "vulnerable": vuln_type is not None,
        "type": vuln_type
    }


def format_result(res):
    if res["vulnerable"]:
        return {
            "payload": res["payload"],
            "status": f"[VULNERABLE] {res['type']}"
        }
    else:
        return {
            "payload": res["payload"],
            "status": "Not Vulnerable"
        }
