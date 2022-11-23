#!/usr/bin/python3
#import phones_ssb
from datetime import datetime,timedelta
import count_phonelines_busyness
import sys

now=datetime.now()

f_start = lambda row : datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
f_end = lambda row : datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')+timedelta(seconds=int(row[9]))
f_conditions = lambda row : row[7]=='Dial' and row[8][0:9] == 'SIP/goip1'  
count_phonelines_busyness.handle_file(sys.argv[1], f_start, f_end, f_conditions,',')

print(datetime.now()-now)