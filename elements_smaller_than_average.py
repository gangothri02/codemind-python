n=int(input())
l=list(map(int,input().split()))
av=sum(l)/n
c=0
for i in l:
    if i<=av:
        c+=1
print(c)