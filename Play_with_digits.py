n=int(input())
l=list(map(int,input().split()))
res=0
for i in l:
    while i>0:
        r=i%10
        res+=r
        i=i//10
        
print(res)