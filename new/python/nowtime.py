import time
import datetime
import pytz
def china():
    tz = pytz.timezone('Asia/Shanghai') #东八区
    t = datetime.datetime.fromtimestamp(int(time.time()), pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')
    return t
