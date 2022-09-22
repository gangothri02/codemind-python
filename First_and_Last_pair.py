n=int(input())
a=list(map(int,input().split()))
if len(a)%2==0:
    l=['']*len(a)
    k=0
    p=1
    for i in range(len(a)//2):
        l[k]=a[i]
        k+=2
    for j in range(len(a)-1,len(a)//2-1,-1):
        l[p]=a[j]
        p+=2
else:
    l=['']*(len(a)+1)
    k=0
    p=1
    for i in range((len(a)//2)+1):
        l[k]=a[i]
        k+=2
    for j in range(len(a)-1,(len(a)//2),-1):
        l[p]=a[j]
        p+=2
    l[-1]=0
for i in l:
    print(i,end=" ")
