n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if i%2:
        m=l.index(i)
        c+=1
        break
s=0
for i in range(0,m):
    s+=l[i]
print(s)