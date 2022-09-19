n=int(input())
a=list(map(int,input().split()))
m=int(input())
dic={}
for i in a:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
c=0
for k,v in dic.items():
    if v==m:
        c+=1
        print(k,end=' ')
if c==0:
    print(-1)