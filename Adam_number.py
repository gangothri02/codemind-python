n=int(input())
m=n**2
m=str(m)
m=m[::-1]
n=str(n)
n=n[::-1]
n=int(n)
r=n**2
r=str(r)
if r==m:
    print("True")
else:
    print("False")