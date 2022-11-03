import sys

D = list(sys.stdin.readline().rstrip())
C = []
for i in D:
    if i != ' ' and not i.isdigit():
        if ord(i) >= 97:
            tmp = (ord(i)-ord('a')+13) % 26 + ord('a')
        else:
            tmp = (ord(i)-ord('A')+13) % 26 + ord('A')
        C.append(chr(tmp))
    else:
        C.append(i)
print(''.join(C))