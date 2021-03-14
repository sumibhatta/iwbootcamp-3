#Write a function to write a comma-separated value (CSV) file.
#It should accept a filename and a list of tuples as parameters.
#The tuples should have a name, address, and age.
#The file should create a header row followed by a row for each tuple.
#If the following list of tuples was passed in:
#[('George', '4312 Abbey Road', 22), ('John', '54 Love Ave',21)]
#it should write the following in the file:
#name,address,age
#George,4312 Abbey Road,22
#John,54 Love Ave,21

def cSV(filename, listoftuple):
    filename =filename[:-4]+".csv"
    print(filename)
    print('name, address, age')
    data = [tuple(str(x) for x in tup) for tup in listoftuple]
    for word in range(len(data)):
        i = data[word]
        toStr =  ', '.join(i) 
        print(toStr)
    # print(listoftuple)
    # 


cSV('README.txt',[('George','4312 Abbey Road',22),('John','54 Love Ave',21)])
