weight = float(input("Enter weight kg : "))
body_fat_weight = float(input("Enter body fat weight kg: "))


body_fat_percentage = (body_fat_weight/weight) * 100

if body_fat_percentage >= 25 and body_fat_percentage <=31:
    print('The person is healthy(women)')
else:
    print('The person is not healthy(women)')