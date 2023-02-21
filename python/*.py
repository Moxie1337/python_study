from typing import Dict

def one_s(param):
    print(*param)

def print_info(info, *, address = None, phone = None):
    print(f'info : {address}, {phone}')

def two(moxie, /, *args, name = None, age = None,  **kwargs):
    print("moxie", moxie)
    print("args", *args)
    print(name, age)
    print(kwargs)
    print_info(1, **kwargs)

f = "moxie"
l = [2, 3, 4]
l1 = [156,465,4,566,10]
d = {'name':'wuyize', 'age': 7}
name = 'frog'
age = 15

# one_s(f)
two(f, l, l1, name = name, age = age, address = "known", phone = "10010")