# Create a list of tuples of first name, last name, and age for your friends
# and colleagues. 
# If you don't know the age, put in None. 
# Calculate the average age, skipping over any None values.
# Print out each name,
# followed by old or young if they are above or below the average age.

friends = [('Sumi','Bhatta',20),('Sum','Bhatt',21),('S','Bha',None)]

sum = 0
countNone = 0
for afriend in friends:
    if afriend[2] != None:
        sum += afriend[2]
    else:
        countNone +=1

average = sum / (len(friends)-countNone)
print(average)

for afriend in friends:
    print(afriend[0],afriend[1])
    if afriend[2] < average:
        print('looks young')
    else:
        print('looks old')