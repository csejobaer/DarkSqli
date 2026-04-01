def analyze_response(response_text, baseline_text):
    score = 0

    errors = ["sql", "mysql", "syntax", "database error"]

    for err in errors:
        if err in response_text.lower():
            score += 2

    # Response length difference
    diff = abs(len(response_text) - len(baseline_text))
    if diff > 50:
        score += 1

    if score >= 2:
        return True

    return False
