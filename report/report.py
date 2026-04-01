def generate(results):
    high = [r for r in results if r["risk"] == "HIGH"]
    medium = [r for r in results if r["risk"] == "MEDIUM"]

    return {
        "total": len(results),
        "high": len(high),
        "medium": len(medium),
        "details": results
    }
