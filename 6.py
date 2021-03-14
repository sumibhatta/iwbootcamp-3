# Create a list with the names of friends and colleagues.
#Search for the name `john` using a for loop. 
#Print 'not found if you didn't find it


friends = ['Sumi', 'Angela','Pramila', 'Usha','John']

flag = False
for name in friends:
    if name == "John":
         flag = True
         break

if flag:
    print("Found")
    
else:
    print("Not found")