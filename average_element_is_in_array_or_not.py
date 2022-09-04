n=int(input())
a=list(map(int,input().split()))
s=sum(a)
y=s//n
for i in a:
    if i==y:
        print("True")
        break
else:
    print('False')
    