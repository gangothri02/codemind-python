n=int(input())
l=list(map(int,input().split()))
m=min(l)
m=str(m)
res=len(m)
c=0
for i in l:
    i=str(i)
    if len(i)==res:
        c+=1
        
print(c)