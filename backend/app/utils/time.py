from datetime import datetime

def calculate_days_between(start: str, end: str) -> int:
    """
    ISO-8601 timestamp stringlerinden gün farkı döner.
    """
    start_date = datetime.fromisoformat(start)
    end_date = datetime.fromisoformat(end)
    return (end_date - start_date).days

def now_iso() -> str:
    return datetime.utcnow().isoformat()
