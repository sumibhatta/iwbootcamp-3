#Write a Python class to find validity of a string of parentheses,
# '(',')',
#'{', '}',
# '[' and ']'.
# These brackets must be close in the correct order,
#for example "()" and "()[]{}" are valid but 
#"[)", "({[)]" and "{{{" are invalid


def validityofBracket(word):
    li =[]
    for char in word:
        if char in ['{','[','(']:
            li.append(char)

        else:
            clChar = li.pop()
            if clChar == '{':
                if char != '}':
                    return False

            if clChar == '(':
                if char != ')':
                    return False
                    
            if clChar == '[':
                if char != ']':
                    return False



m = validityofBracket('{{[]}}()')

if m == False:
    print('Not Valid')

else:
    print('Valid')