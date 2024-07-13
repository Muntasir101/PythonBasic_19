# for loop
for i in range(2):
    print(i, "Hello world!!")

for _ in range(2):
    print("Hello Dhaka!!")

# break
for i in range(20):
    if i == 5:
        break
    print(i, "Hello Mirpur!!")

# continue
for i in range(20):
    if i % 2 == 0:
        break
    print(i, "Hello Dhanmondi!!")
"""
i starts at 0
if 0 % 2 == 0: return True
"""

for i in range(2, 10):
    print(i, "Hello Rain!!")


for i in range(2, 10, 3):
    print(i, "Hello Sun!!")
