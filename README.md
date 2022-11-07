# count_phonelines_busyness
This script helps to count how much time how many lines was occupied. You need calls log where starting 
times of calls go in chronlogical order:
call_1   [------------------]
call_2
...
call_n             [----------------]
                            [---]
                               [---------]
0     ___
1        |_________            ___   _______|
2                  |________   _|   |_| 
3                           |_|   
There is two types of events - first: start of call when quantity of simultaneously occupied lines is increasing
and second: when quantity of simultaneousely occupied lines is decreasing. So we need to go in cronological 
order and count such intervals for each quantity of occupied lines.
