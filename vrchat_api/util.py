from datetime import datetime

def strptime(t):
    return datetime.strptime(t, "%Y-%m-%dT%H:%M:%S.%fZ")
