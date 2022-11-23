# count_phonelines_busyness
you need to view this file in raw view mode to display the scheme

This script helps to count how much time how many phone lines was occupied. You need calls log where starting 
times of calls go in chronlogical order:
call_1   
call_2
...
call_n

              [------------------------------------]
                           [--------]
                                [---------]
0     ________                                      _________
1             |____________                ________|
2                          |____     _____|   
3                               |___|
                                
There is two types of events - first: start of call when quantity of simultaneously occupied lines is increasing
and second: end of call  when quantity of simultaneousely occupied lines is decreasing. So we need to go in cronological 
order and count such intervals for each quantity of occupied lines.


russian:

Этот скрипт помогает посчитать как долго были заняты одновременно несколько телефонных линий: сколько времени одна, сколько дв и т.д
скрипту нужен лог файл, где записи о звонках расположены в хронологическом порядке и из каждой записи можно извлечь время начала,
окончания звонка и его длительность.

при анализе файла используется следующий подход: последовательно перебирая записи о звонках выделяем - события о начале звонка-
когда количество занятых линий увеличивается и об окончании, когда количество занятых линий уменьшается. При этом все события окончаний
звонка помещааются в стек в хронологическом порядке ожидают там своей обработки до тех пор пока придет следующее 
более позднее, чем ожидающие окончания,событие начала звонка либо будут обработаны все звонки

