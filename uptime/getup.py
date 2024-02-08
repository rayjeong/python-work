#!/usr/bin/env python

def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        return uptime_seconds

def format_uptime(uptime_seconds):
    days = uptime_seconds // (24 * 3600)
    hours = (uptime_seconds % (24 * 3600)) // 3600
    minutes = (uptime_seconds % 3600) // 60
    seconds = uptime_seconds % 60
    return f"{int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds"

if __name__ == "__main__":
    uptime_seconds = get_uptime()
    formatted_uptime = format_uptime(uptime_seconds)
    print("System Uptime:", formatted_uptime)
