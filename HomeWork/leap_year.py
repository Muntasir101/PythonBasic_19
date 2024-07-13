def leap_year(year):
   # year = int(input("year: "))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        # print("Leap Year")
        return "Leap Year"
    else:
        # print("Not leap year")
        return "Not Leap Year"


print(leap_year(int(input("enter year: "))))

print("Code Execution done.")
