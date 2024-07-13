number_1 = int(input("Enter Number 1: "))
number_2 = int(input("Enter Number 2: "))


def summation():
    result = number_1 + number_2
    print(result)


def subtraction():
    result = number_1 - number_2
    print(result)


subtraction()
summation()


# function parameters

def user_name(name="test user"):
    print('Hello', name)


user_name("Smith")
user_name("John")
user_name()


# return
def multiplication():
    return number_1 * number_2


# print(multiplication())
multiple_result = multiplication()
#print(multiple_result)

# multiplication = 100

report = multiplication() + 10
print(report)