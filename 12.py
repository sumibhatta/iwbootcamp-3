# Create a function, is_palindrome, to determine if a supplied word is
# the same if the letters are reversed.

def is_palindrome(word):
    if word == word[::-1]:
        print('Is palindrome')
    else:
        print('Is not palindrome')

is_palindrome('ama')