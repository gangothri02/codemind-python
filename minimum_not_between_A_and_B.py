n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=max(l)
d=0
for i in l:
    if i<a or i>b:
        d+=1
        if i<c:
            c=i
if d==0:
    print(-1)
else:
    print(c)