n=int(input())
a=list(map(int,input().split()))
b=set(a)
c=0
for i in b:
    c+=i
print(c)