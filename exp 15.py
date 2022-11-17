list1=input("Enter the 1st list:")
list2=input("Enter the 2st list:")
x=len(list1)
y=len(list2)
if x==y:
    print("The list are of same length")
else:
    print("The list is not same length:")
x=sum(list1)
y=sum(list2)
if x==y:
     print("List sums to same value")
else:
     print("List not sums to same value")
