import aiohttp
import asyncio
import time

from scanner.payloads import get_all_payloads
from scanner.core import analyze, format_result
from scanner.utils import extract_params, inject_payload
from scanner.fingerprint import fingerprint_db
from scanner.ml_model import train_model, predict_anomaly
from scanner.encoder import encode_payload


async def fetch(session, url):
    start = time.time()
    async with session.get(url) as response:
        text = await response.text()
    end = time.time()
    return text, (end - start)


async def scan_target(url):
    results = []
    payloads = get_all_payloads()

    parsed, params = extract_params(url)

    if not params:
        print("[!] No parameters found in URL")
        return []

    model = train_model()

    async with aiohttp.ClientSession() as session:

        baseline_text, _ = await fetch(session, url)

        tasks = []
        meta = []

        for param in params:
            for payload in payloads:

                encoded_payload = encode_payload(payload)

                test_url = inject_payload(parsed, params, param, encoded_payload)

                tasks.append(fetch(session, test_url))
                meta.append((param, payload))

        responses = await asyncio.gather(*tasks)

        for i, (res_text, res_time) in enumerate(responses):
            param, payload = meta[i]

            analysis = analyze(payload, res_text, baseline_text, res_time)
            formatted = format_result(analysis)

            # 🔍 DB fingerprint
            db = fingerprint_db(res_text)

            # 🤖 ML anomaly
            anomaly = predict_anomaly(model, len(res_text))

            # 🎯 confidence score
            score = 0
            if "VULNERABLE" in formatted["status"]:
                score += 70
            if anomaly:
                score += 20
            if db != "Unknown":
                score += 10

            formatted.update({
                "param": param,
                "db": db,
                "anomaly": anomaly,
                "confidence": f"{score}%"
            })

            results.append(formatted)

    return results
