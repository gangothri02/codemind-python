s=input()
a=input()
for i in s:
    if i==a:
        print("True")
        print(s.index(i))
        break
else:
    print("False")