n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
        if c==2:
            s+=1
print(s)