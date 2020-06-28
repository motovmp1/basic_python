values = [1, 2, 3, "hello", "golden", 4, 5.6]

# list is a data type allow many different values

# can print use index inside the list
print(values[0:])
values.append("hello")

print(values[0:])


# this is hold the key not the index.....take care
dic = {1: "hello", 2: "Vini", "Name": "Vinicius Miranda de Pinho"}
print(dic)
print(dic[1])
# here is the key that hold inside the dic
print(dic["Name"])

print(f'This is the for name: -->  {dic["Name"]}')

# here is empty
dic2 = {}

print("========================================")
print(dic2)
print("here is empty list")
print("=========================================")

dic2["Firstname"] = "Vinicius"
dic2["Lastname"] = "Pinho"
print("\n\n\n")



print("========================================")
print(dic2)
print("here is dic with new values")
print("=========================================")