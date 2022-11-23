import sys

N = int(sys.stdin.readline())
meetings = []
for i in range(N):
    meetings.append(tuple(map(int, sys.stdin.readline().split())))

meetings.sort(key = lambda x:x[0])
meetings.sort(key = lambda x:x[1])

cnt = 0
end = 0
for i in meetings:
    if end <= i[0]:
        end = i[1]
        cnt += 1
print(cnt)