n=int(input())
l=list(map(int,input().split()))
k=int(input())
s=0
m=l.index(k)
for i in range(0,m+1):
    s+=l[i]
print(s)
