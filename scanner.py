def scan(data):
    attacks = {
        "SQL Injection": [
            "select",
            "drop",
            "union",
            "' or '1'='1",
            '" or "1"="1'
        ],
        "XSS": [
            "<script>",
            "</script>",
            "alert("
        ]
    }

    for attack, patterns in attacks.items():
        for pattern in patterns:
            if pattern.lower() in data.lower():
                return f"⚠ {attack} ATTACK DETECTED"

    return "✅ No Suspicious Activity Found"
