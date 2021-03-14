# Write a function, is_prime, that takes an integer and 
# returns True if the number is prime and 
# False if the number is not prime.

def is_prime(n):
    flag = 0
    for num in range(2, n):
        if n%num == 0:
            flag = 1
            break
    if flag == 1:
        print('Is Not Prime')
    else:
        print('Is Prime')

is_prime(13)