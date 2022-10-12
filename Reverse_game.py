n=int(input())
l=list(map(int,input().split()))
c=0
res=[]
for i in l:
    i=str(i)
    j=i[::-1]
    res.append(int(j))
for i in res:
    print(i,end=" ")