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

���� ������ �������� ��������� ��� ����� ���� ������ ������������ ��������� ���������� �����: ������� ������� ����, ������� �� � �.�
������� ����� ��� ����, ��� ������ � ������� ����������� � ��������������� ������� � �� ������ ������ ����� ������� ����� ������,
��������� ������ � ��� ������������.

��� ������� ����� ������������ ��������� ������: ��������������� ��������� ������ � ������� �������� - ������� � ������ ������-
����� ���������� ������� ����� ������������� � �� ���������, ����� ���������� ������� ����� �����������. ��� ���� ��� ������� ���������
������ ����������� � ���� � ��������������� ������� ������� ��� ����� ��������� �� ��� ��� ���� ������ ��������� 
����� �������, ��� ��������� ���������,������� ������ ������ ���� ����� ���������� ��� ������

