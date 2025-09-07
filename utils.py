# utils.py
from datetime import datetime

def is_youtube(url: str) -> bool:
    return url.startswith("https://www.youtube.com") or url.startswith("https://youtu.be")

def time_valid(hhmm: str) -> bool:
    try:
        h, m = map(int, hhmm.split(":"))
        return 0 <= h < 24 and 0 <= m < 60
    except:
        return False

def is_vote_time_reached(vote_time: str) -> bool:
    """Belirlenen vote_time ile şu anki zamanı karşılaştırır"""
    if not vote_time:
        return False
    now = datetime.now()
    h, m = map(int, vote_time.split(":"))
    return now.hour > h or (now.hour == h and now.minute >= m)