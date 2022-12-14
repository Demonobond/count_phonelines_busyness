#!/usr/bin/python3
import csv
from datetime import datetime,timedelta

durations=[]
ends = []
current_level=-1
previous_time = datetime(1,1,1,0,0)



def count_end():
    global current_level, ends, previous_time, durations
    durations[current_level] += ends[0]-previous_time
    previous_time = ends[0]
    ends.pop(0)
    current_level -= 1

def handle_file(file_to_handle, f_start, f_end, f_conditions,delimiter) :
    counter = 0
    global current_level, ends,previous_time,ends, durations
    with open(file_to_handle, 'r',encoding='cp1251') as f:
        reader = csv.reader(f,delimiter=delimiter)
        next(reader) # Skip the header row.
        for row in reader:
            counter += 1
            start = f_start(row)
            end = f_end(row)
            duration = end - start
            if duration == timedelta(seconds=0): continue
            if f_conditions(row):
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


