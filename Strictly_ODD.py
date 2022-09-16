n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if i%2:
        c+=1
d=0
for i in range(len(a)):
    if a[i]%2 and i%2:
        d+=1
if c==d:
    print("True")
else:
    print("False")