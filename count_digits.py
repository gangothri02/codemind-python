n=int(input())
l=list(map(int,input().split()))
for i in l:
    i=str(abs(i))
    print(len(i),end=" ")