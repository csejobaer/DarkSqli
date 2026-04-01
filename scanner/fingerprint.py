def fingerprint_db(response_text):
    text = response_text.lower()

    if "mysql" in text:
        return "MySQL"
    elif "postgresql" in text:
        return "PostgreSQL"
    elif "ora-" in text:
        return "Oracle"
    elif "sqlite" in text:
        return "SQLite"
    else:
        return "Unknown"
