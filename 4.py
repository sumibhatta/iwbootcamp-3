# Create a list. Append the names of your colleagues and friends to it.
# Has the id of the list changed? Sort the list. What is the first item on
# the list? What is the second item on the list?

lis = ['Sumi']
print(id(lis))
lis.append('Pramila')
lis.append('Kusum')
lis.append('Ange')
lis.append('Samyoga')
lis.append('Shristi')
print(lis)
print(id(lis))
sortedList = sorted(lis)

print(lis)
print(sortedList)


print("Id of list before and after sorting")
print(id(lis))
print(id(sortedList))

print("Id of first item before and after sorting")
print(id(lis[0]))
print(id(sortedList[0]))

print("Id of second item before and after sorting")
print(id(lis[1]))
print(id(sortedList[1]))