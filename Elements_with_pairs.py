n=int(input())
a=list(map(int,input().split()))
if len(a)%2:
    a.append(0)
for i in a:
    print(i,end=" ")