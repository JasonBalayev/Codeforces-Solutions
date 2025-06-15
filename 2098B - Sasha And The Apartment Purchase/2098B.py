import sys

def count_houses(a,k):
    a.sort()
    n=len(a)
    ranges=[]
    for i in range(n):
        if n-(2*min(i,n-1-i)+1)<=k:
            v=a[i]
            ranges.append((v,v))
    for i in range(n-1):
        if n-(2*min(i+1,n-1-i))<=k:
            ranges.append((a[i],a[i+1]))
    if not ranges:
        return 0
    ranges.sort()
    res=0
    l,r=ranges[0]
    for x,y in ranges[1:]:
        if x>r:
            res+=r-l+1
            l,r=x,y
        else:
            r=max(r,y)
    res+=r-l+1
    return res

def solve():
    n,k=map(int,sys.stdin.readline().split())
    arr=list(map(int,sys.stdin.readline().split()))
    print(count_houses(arr,k))

T=int(sys.stdin.readline())
for _ in range(T):
    solve()