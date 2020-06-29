class Myclass:
    name = "Vinicius"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def suma(self, a, b):
        print(a + b)


x = Myclass("Vini", 40)
print(x.name)
x.suma(10, 20)
print(x.age)




