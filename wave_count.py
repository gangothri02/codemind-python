n=int(input())
l=list(map(int,input().split()))
c=0
if n%2==0:
    for i in range(0,n-3,2):
        if l[i]<l[i+1] and l[i+1]>l[i+2]:
           c+=1
    if c==n//2-1:
        print(c)
    else:
        print(-1)
else:
    for i in range(0,n-2,2):
        if l[i]<l[i+1] and l[i+1]>l[i+2]:
           c+=1
    if c==n//2:
        print(c)
    else:
       print(-1)