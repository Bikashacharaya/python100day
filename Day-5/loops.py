#Average Height 

lst=[180,120,135,140,200]
# a=len(lst)
# b=sum(lst)
# avg=b/a
# print(avg)
addition=0
for i in lst:
    addition=i+addition
print(addition)
element=0
for i in lst:
    element+=1
print(element)    

total_average=addition/element
print("The average of list are",total_average)
