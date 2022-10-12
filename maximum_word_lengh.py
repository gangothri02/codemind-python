s=input()
s=s.split(' ')
res=0
for i in s:
    if len(i)>res:
        res=len(i)

print(res)
    