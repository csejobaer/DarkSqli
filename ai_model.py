def predict(response, baseline):
    score = 0

    keywords = ["sql", "error", "mysql", "syntax", "warning"]

    for k in keywords:
        if k in response.lower():
            score += 2

    diff = abs(len(response) - len(baseline))

    if diff > 100:
        score += 1

    if score >= 3:
        return "HIGH"
    elif score == 2:
        return "MEDIUM"
    else:
        return "LOW"
