# Write code that will print out the anagrams (words that use the same
# letters) from a paragraph of text.

para = "bade acre bead beat beta beast tabu tuba care beats race"
anagrams = []
lis = ''.join(para).split()
duplist = lis
# print(lis)
# print(duplist)

A = [''.join(sorted(word)) for word in duplist]

# li=[]

# for i in range(len(duplist)):
#     li.append([])
#     li[i] = sorted(duplist[i]) #Converted into list

# print(li)

# le = []
# for word in range(len(li)):
#     listToSTR = ''.join(map(str, li[word]))
#     print(listToSTR)
#     le.append(listToSTR) #reverted to string after sorting

# print(le)
dict = {}
for i, e in enumerate(A):
    dict.setdefault(e, []).append(i) #Store the values of indexes in A

for index in dict.values():
		print([lis[i] for i in index]) #print the grouped indexes from lis