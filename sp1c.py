a=eval(input())
if len(a)==0:
        print("empty")
for i in a:
        if type(i)!=int:
               print("mixed")
               break
else:
        print("yes")
print()
