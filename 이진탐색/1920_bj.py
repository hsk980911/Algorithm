import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

A.sort()

def Binary_search(arr, target, left, right):
    if left > right:
        return 0
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return 1
    elif target > arr[mid]:
        return Binary_search(arr, target, mid+1, right)
    else:
        return Binary_search(arr, target, left, mid-1)
    
for i in B:
    print(Binary_search(A, i, 0, len(A)-1))
        
        