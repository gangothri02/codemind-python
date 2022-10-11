n=int(input())
l=list(map(int,input().split()))
m=[]
for i in range(0,n-1,2):
    for j in range(l[i+1]):
        m.append(l[i])
for i in m:
    print(i,end=" ")