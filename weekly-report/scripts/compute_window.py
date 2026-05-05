#!/usr/bin/env python3
"""Print the default weekly-report window: last Wed 16:00 local -> now."""
from datetime import datetime, timedelta

now = datetime.now()
d = (now.weekday() - 2) % 7
if d == 0 and now.hour < 16:
    d = 7
since = (now - timedelta(days=d)).replace(hour=16, minute=0, second=0, microsecond=0)
print(f"{since.strftime('%Y-%m-%d %H:%M')} -> {now.strftime('%Y-%m-%d %H:%M')}")
