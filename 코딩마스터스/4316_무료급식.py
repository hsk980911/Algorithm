import sys

N = int(sys.stdin.readline())
order = []
for _ in range(N):
    age, name = sys.stdin.readline().split()
    order.append((int(age), name))

sorted_order = sorted(order, key=lambda x:x[0], reverse=True)
print(sorted_order)
for i in sorted_order:
    print(i[1])