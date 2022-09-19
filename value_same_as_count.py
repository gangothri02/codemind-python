n=int(input())
a=list(map(int,input().split()))
dic={}
for i in a:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
c=0
for k,v in dic.items():
    if k==v:
        c+=1
print(c)
    
    