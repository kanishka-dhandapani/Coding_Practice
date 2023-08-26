# METHOD-1
def checkLeapYear(year):
    if (year%400 == 0 or year%100 != 0) and year%4 == 0:
        print("Leap Year")
    else:
        print("Not a Leap Year")

year = int(input()) 
checkLeapYear(year)

# METHOD-2
def checkLeapYear(year):
    if (year%400 == 0 or year%100 != 0) and year%4 == 0:
        return "Leap Year" 
    else:
        return "Not a Leap Year"

year = int(input()) 
result = checkLeapYear(year)
print(result)
