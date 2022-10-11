n=int(input())
l=list(map(int,input().split()))
s=0
e=0
for i in l:
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        e+=i
        s+=1
t=e/s
print("{:.2f}".format(t))
        