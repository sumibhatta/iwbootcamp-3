# Write an if statement to determine whether a variable holding a year is
# a leap year.

def isNewYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("{} is a leap year".format(year))
            else:
                print("{} is not a leap year".format(year))
        else:
            print("{} is a leap year".format(year))
    else:
        print("{} is not a leap year".format(year))


isNewYear(2000)
