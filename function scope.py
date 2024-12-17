#first attempt :
def increment_counter():
    i = 10
    counter = 0
    while i > 0 :
        counter += 1
        print(counter)
        i -= 1


increment_counter()

#taking help from chatgpt
counter = 0
def increment_counter():
    global counter
    counter += 1
    print(f"Counter inside = {counter}")

increment_counter()
increment_counter()
increment_counter()
increment_counter()

print(f"Counter outside = {counter}")