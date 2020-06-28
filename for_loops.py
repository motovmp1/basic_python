import time

# this is foor loop to run inside each list

obj = [10, 20, 30, 40, "vini"]
counter = 0
for i in obj:
    print(i)
    counter += 1
    print(f'Passei uma vez pelo loop: {counter}')
    time.sleep(1)


