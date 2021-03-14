#Write a python class
#to find the three elements that sum to zero
#from a list of n real numbers.
#Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
#Output : [[-10, 2, 8], [-7, -3, 10]]

class sumToZero:

    def sumZero(self, arr):

        i= 0
        li = []
        while i<len(arr):
            num1 = arr[i]
            j = i+1
            while j< len(arr):
                num2 = arr[j]
                k = j+1
                while k<len(arr):
                    num3 = arr[k]
                    
                    sum = num1+num2+num3
                    if sum == 0:
                        li.append([num1,num2,num3])
                        

                    k= k+1
                j=j+1
            i=i+1
        print(li)
summm = sumToZero()
summm.sumZero([-25, -10, -7, -3, 2, 4, 8, 10])