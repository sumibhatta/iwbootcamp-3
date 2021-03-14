# Write a function that takes camel-cased strings (i.e.
# ThisIsCamelCased), and converts them to snake case (i.e.
# this_is_camel_cased). Modify the function by adding an argument,
# separator, so it will also convert to the kebab case
# (i.e.this-is-camel-case) as well.

def caseConverter(word, separator):
    converted = ""
    start = 0
    for i in range(1,len(word)-1):
        if word[i].isupper():
            # converted = converted + camel[start:i] + '_'
            converted = converted + word[start:i] + separator
            start = i
    converted = converted + word[start:]
    return converted.lower()

print(caseConverter('HeyYouHowAreYou', "-"))
