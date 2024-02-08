import re
from datetime import timedelta

def parse_uptime(output):
    uptime_pattern = re.compile(r'up\s+(?:(?P<days>\d+)\s+days?,\s+)?(?:(?P<hours>\d+):)?(?P<minutes>\d+)\s+min')
    matches = uptime_pattern.search(output)
    if matches:
        days = int(matches.group('days')) if matches.group('days') else 0
        hours = int(matches.group('hours')) if matches.group('hours') else 0
        minutes = int(matches.group('minutes'))
        total_uptime = timedelta(days=days, hours=hours, minutes=minutes)
        return total_uptime
    else:
        return None

if __name__ == "__main__":
    uptime_output = " 15:36:27 up 1 days,  4:28,  1 user,  load average: 0.00, 0.00, 0.00"
    uptime = parse_uptime(uptime_output)
    if uptime:
        print("System uptime:", uptime)
    else:
        print("Failed to parse uptime information.")
