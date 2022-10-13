s=input()
l=['a','e','i','o','u']
for i in s:
    if i in l:
        m=l.index(i)
        del l[m]
if l==[]:
    print(0)
else:
    for i in l:
        print(i,end=" ")