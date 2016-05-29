def double_name(name):
    new_name = name + " " + name
    return new_name

def caller(func, val):
    return func(val)

my_name = input("What's your name?\n")

for i in range(4):
    print(caller(double_name, my_name))
