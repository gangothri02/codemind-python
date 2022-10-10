n=int(input())
l=list(map(int,input().split()))
t=[]
s=[]
for i in l:
    if i%2==0:
        t.append(i)
    else:
        s.append(i)
st=t+s
for i in st:
    print(i,end=" ")