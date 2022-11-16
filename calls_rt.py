#!/usr/bin/python3
#import phones_ssb
from datetime import datetime,timedelta
import count_phonelines_busyness
import sys

now=datetime.now()

f_start = lambda row : datetime.strptime(row[0]+" "+ row[1], '%Y-%m-%d %H:%M:%S')
f_end = lambda row : datetime.strptime(row[0]+" "+ row[1], '%Y-%m-%d %H:%M:%S')+timedelta(seconds=sum(x * int(t) for x, t in zip([3600, 60, 1], row[9].split(":"))))
f_conditions = lambda row : row[7]=='Исходящий' and row[8]=='успешный'
count_phonelines_busyness.handle_file(sys.argv[1], f_start, f_end, f_conditions,';')

print(datetime.now()-now)