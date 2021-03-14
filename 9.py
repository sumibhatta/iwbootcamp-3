# Write a binary search function.
# It should take a sorted sequence and the item it is looking for. 
# It should return the index of the item if found.
# It should return -1 if the item is not found.

def binary_search(sortedSeq, item, low, high):
    mid = (low+(high-low)/2)
    
    if high<low:
        return -1
        
    if sortedSeq[mid] == item:
        print('Key Found')
        return mid
    elif item < sortedSeq[mid]:

        return binary_search(sortedSeq,item,low, mid-1)
    
    elif item > sortedSeq[mid]:
        return binary_search(sortedSeq,item,mid+1,high)
    

k = binary_search([1,2,3,4,5,6,7,8,9,10],2,0,9)
print(k)