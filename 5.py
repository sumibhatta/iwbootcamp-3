# Create a tuple with your first name, last name, and age.
# Create a list,people, and append your tuple to it.
# Make more tuples with the corresponding information from your friends 
# and append them to the list.
# Sort the list.
# When you learn about sort method,
# you can use the key parameter to sort by any field in the tuple,
# first name, last name, or age.

my_tuple = ('Sumi', 'Bhatta',20)
people = []
people.append(my_tuple)


tup2 = ('Sum', 'Bha', 21)
people.append(tup2)

# lis = sorted(people)
# print(lis)
# print(people)

key = lambda x: x[2]

people.sort(key = key)
print(people)