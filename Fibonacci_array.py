n=int(input())
l=list(map(int,input().split()))
if n>2:
    for i in range(2,n):
        if l[i]!=l[i-1]+l[i-2]:
            print("no")
            break
    else:
        print("yes")
else:
    print("no")
    