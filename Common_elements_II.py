n,m=map(int,input().split())
l=list(map(int,input().split()))
p=list(map(int,input().split()))
l1=[]
p1=[]
for i in l:
    if i not in l1:
        l1.append(i)
for i in p:
    if i not in p1:
        p1.append(i)
c=0
s=[]
for i in l1:
    if i not in p1:
       s.append(i)
for i in p:
    if i not in l:
       s.append(i)
for i in s:
    print(i,end=" ")