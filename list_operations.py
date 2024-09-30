mylist=[]
n=int(input ("Enter Number of Elements:"))
print("Enter list Elements")
for i in range(0,n):
 e=input()
 mylist.append(e)
print("List Elements:",mylist)
print("Fourth Element of the List:",mylist[3])
print("Elements from 3rd to Last:",mylist[2:])
print("Last Element:",mylist[-1])
#insert new Element in index 3
n=int(input("Enter New Element to be Inserted:"))
mylist.insert(3,n)
print("List Elements:",mylist)
print("Length of List:",len(mylist))
list2=[8,9,4]
mylist=mylist+list2
print("Elements of List:",mylist)
print("Length of List:",len(mylist))