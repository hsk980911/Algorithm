import sys

x, y = map(int, sys.stdin.readline().split())

weekday = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

days = 0
for i in range(1, x):
    if i == 2:
        days += 28
    elif i in [1,3,5,7,8,10,12]:
        days += 31
    else:
        days += 30
days += y-1

print(weekday[days%7])