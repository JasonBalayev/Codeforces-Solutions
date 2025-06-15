import sys

def solve():
    n,k=map(int,sys.stdin.readline().split())
    s=sys.stdin.readline().strip()
    c0=s.count('0')
    c1=n-c0
    y=n//2-k
    ok=c0>=y and c1>=y and (c0-y)%2==0 and (c1-y)%2==0
    print("YES" if ok else "NO")

T=int(sys.stdin.readline())
for i in range(T):
    solve()