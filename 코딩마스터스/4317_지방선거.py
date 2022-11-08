import sys
from collections import Counter

N = int(sys.stdin.readline())
votes = [int(sys.stdin.readline()) for _ in range(N)]
votes_c = Counter(votes)

sorted_votes = sorted(votes_c.items(), key=lambda x:x[0])
sorted_votes = sorted(sorted_votes, key=lambda x:x[1], reverse=True)
print(sorted_votes[0][0])