class Calculator:
    num = 100

    def getData(self):
        print("I am inside de method in class 1")


# need to create a instance
obj_create = Calculator()


obj_create.getData()
print(obj_create.num)

