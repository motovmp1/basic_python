class Calculator:
    # this is variable inside the class
    num = 100

    def __init__(self, a, b):
        print("I am call automatic when object is created")
        self.first_value = a
        self.second_value = b
        self.result = 0

    def getData(self):
        print("I am inside de method in class 1")

    def summation(self):
        print("I am inside the summation")
        self.result = (self.first_value + self.second_value)
        print(f'this is sum result: {self.result}')


# need to create a instance
obj_create = Calculator(2, 3)

obj_create.getData()
print(obj_create.num)
obj_create.summation()

print("===================================")

obj1_create = Calculator(3, 4)
obj1_create.getData()
obj1_create.summation()
