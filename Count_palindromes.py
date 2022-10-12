n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    i=str(i)
    j=i[::-1]
    if int(i)==int(j):
        c+=1
print(c)