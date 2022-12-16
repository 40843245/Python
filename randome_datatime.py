from datetime import datetime
import time
import random

MINTIME = datetime(2019,8,6,8,14,59)
MAXTIME = datetime(2020,8,6,8,14,59)

mintime_ts = int(time.mktime(MINTIME.timetuple()))
maxtime_ts = int(time.mktime(MAXTIME.timetuple()))


for _ in range(5):
    random_ts = random.randint(mintime_ts, maxtime_ts)
    RANDOMTIME = datetime.fromtimestamp(random_ts)
    print(RANDOMTIME)