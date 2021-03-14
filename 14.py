#Write a function that reads a CSV file.
# It should return a list of dictionaries,
# using the first row as key names, and each subsequent
#row as values for those keys.
#For the data in the previous example it would return:
#[{'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, {'name':
#'John', 'address': '54 Love Ave', 'age': 21}]

def readCSV(file):
    file = open("testing.txt")
    lisst = []
    lines = file.readlines()
    headers = lines[:1][0].replace('\n','').split(',')
    tvalues = lines[1:]

    for line in tvalues:
        values = line.replace("\n","").split(",")
        person = {}
        for i, header in enumerate(headers):
            person[header] = values[i]

        lisst.append(person)

    return lisst

print(readCSV("testing.txt"))
