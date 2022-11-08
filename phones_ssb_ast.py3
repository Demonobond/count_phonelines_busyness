#!/usr/bin/python3
import csv
from datetime import datetime,timedelta

durations=[]
ends = []
current_level=-1
counter = 0
previous_time = datetime(1,1,1,0,0)
now=datetime.now()

def count_end():
    global current_level, ends,previous_time
    durations[current_level] += ends[0]-previous_time
    previous_time = ends[0]
    ends.pop(0)
    current_level -= 1

with open('/home/user/phones/mobiles_oct.csv', 'r',encoding='cp1251') as f:
    reader = csv.reader(f,delimiter=',')
    next(reader) # Skip the header row.
    for row in reader:
            counter +=1
            #if counter>10 : break
            duration=int(row[9])
            if duration == 0: continue
            if row[7] != 'Dial' : continue
            if row[8][0:9] == 'SIP/goip3' : continue
            start = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
            end = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')+timedelta(seconds=duration)
            while len(ends)>0 and (ends[0]) < start : count_end()
            if len(durations)-1 <= current_level : durations.insert(current_level+1,timedelta(seconds=0))
            if current_level != -1 : durations[current_level] += start - previous_time
            current_level +=1
            previous_time = start
            i=0
            while i<len(ends) and ends[i] < end : i += 1
            ends.insert(i, end)
    while len(ends)>0 : count_end()
        
for idx,dur in enumerate(durations):
   print(str(idx+1)+" "+str(dur.total_seconds()))

print(datetime.now()-now)