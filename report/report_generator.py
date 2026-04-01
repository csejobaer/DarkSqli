def generate_report(target, results):
    html = f"""
    <html>
    <head>
    <style>
    body {{
        background-color: #0d0d0d;
        color: #00ff99;
        font-family: monospace;
    }}
    h1 {{
        color: red;
    }}
    .vuln {{
        color: #ff4d4d;
    }}
    .safe {{
        color: #00ff99;
    }}
    </style>
    </head>
    <body>

    <h1>☠ DarkSqli PRO Report ☠</h1>
    <p>Target: {target}</p>
    <hr>
    """

    for r in results:
        cls = "vuln" if "VULNERABLE" in r["status"] else "safe"

        html += f"""
        <p class="{cls}">
        Param: {r.get('param')} <br>
        Payload: {r['payload']} <br>
        Status: {r['status']} <br>
        DB: {r['db']} <br>
        Anomaly: {r['anomaly']} <br>
        Confidence: {r['confidence']}
        </p>
        <hr>
        """

    html += "</body></html>"

    with open("report.html", "w") as f:
        f.write(html)
