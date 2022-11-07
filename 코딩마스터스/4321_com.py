import sys

N = int(sys.stdin.readline())
scores = [tuple(sys.stdin.readline().split()) for _ in range(N)]

scores = sorted(scores, key=lambda x:x[0], reverse=True)
scores = sorted(scores, key=lambda x:x[1], reverse=True)

for i in scores:
    print(i[0], end = ' ')