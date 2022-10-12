n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
m=max(l)
d=0
for i in l:
    if i>=a and i<=b:
        d+=1
        if i<m:
            m=i
if d!=0:
    print(m)
else:
    print(-1)
