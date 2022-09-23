n=int(input())
a=list(map(int,input().split()))
d=[]
for i in a:
    if i not in d:
        d.append(i)
        print(i,a.count(i),end=' ')