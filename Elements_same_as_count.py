n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(n):
    c=1
    for j in range(n):
        if i!=j and a[i]==a[j]:
            c+=1
    if c==a[i]:
        l.append(a[i])
m=[]
if l==[]:
    print(-1)
else:
    for i in l:
        if i not in m:
            m.append(i)
    for j in m:
        print(j,end=" ")
        
        
            
            