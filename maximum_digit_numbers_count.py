n=int(input())
l=list(map(int,input().split()))
s=[]
res=0
for i in l:
    if abs(i) not in s:
        s.append(i)
        i=str(i)
        if len(i)>res:
            res=len(i)
for i in s:
    i=str(i)
    if len(i)==res:
        print(i,end=" ")