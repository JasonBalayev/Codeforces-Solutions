import sys

def min_operations(n:int,k:int)->int:
    if n<=k:
        return 1
    max_even=k-1
    if n%2==0:
        return(n+max_even-1)//max_even
    else:
        remaining=n-k
        return 1+(remaining+max_even-1)//max_even

def solve():
    n,k=map(int,sys.stdin.readline().split())
    print(min_operations(n,k))

T=int(sys.stdin.readline())
for i in range(T):
    solve()