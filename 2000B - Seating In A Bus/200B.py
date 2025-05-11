import sys

def solve():
    n=int(sys.stdin.readline())
    seats=list(map(int, sys.stdin.readline().split()))
    s=set()
    b=True
    if n==0:
        print("YES")
        return
    for i in range(n):
        x=seats[i]
        if i==0:
            s.add(x)
        else:
            occupied=False
            if (x-1) in s:
                occupied=True
            if (x+1) in s:
                occupied=True
            if not occupied:
                b=False
            s.add(x)
    if b:
        print("YES")
    else:
        print("NO")

T=int(sys.stdin.readline())
for i in range(T):
    solve()