import time

num = [1, 2, 3, 4, 5, 6]

for index, value in enumerate(num):
    print(index, "-->", +  value)
    time.sleep(0.2)


num1 = [1, 2, 3, 4, 5, 6]
summation = 0
for value1 in num1:
    summation = summation+value1
print(summation)


fruits = ["apple", "orange", "grapes"]

for value in fruits:
    print(value)
else:
    print("No fruits left")


num = 10
summation = 0
i = 1

while i < num:
    summation = summation + i
    i += 1
print("total is ", summation)

