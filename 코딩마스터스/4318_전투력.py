import sys

N = int(sys.stdin.readline())

power = list(map(int, sys.stdin.readline().split()))
power.sort()

max_power = power[-1]
for i in range(len(power)):
    tmp = (N-i) * power[i]
    if max_power < tmp: max_power = tmp
    
print(max_power)