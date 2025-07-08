def classify_risk(name: str, sources: dict) -> tuple[str, str, str]:
    name = name.lower()

    if name in [n.lower() for n in sources.get("ofac", [])]:
        return "high", "Match found in OFAC list", "OFAC SDN List"
    elif name in [n.lower() for n in sources.get("watchlist", [])]:
        return "medium", "Mentioned in watchlist", "Interpol Watchlist"
    return "none", "", ""