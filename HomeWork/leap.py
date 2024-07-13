x = int(input("Welcome! Please mention the year you want to check: "))

if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
    print("The year ", x, " is a leap year")
else:
    print("The year ", x, " is not a leap year")