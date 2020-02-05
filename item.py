l=[ ]
while 1:
         item==input('enter item')
         l.append(item)
         n=input('do you want to continue y/n')
         if n.lower()=='n':
                                 break
l.sort(reverse=True,key=len)        
print(l)
                
