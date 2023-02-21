def bread(func):
    def wrapper():
        print("</'''''''\>")
        func()
        print("<\_______/>")
    return wrapper

def ingredients(func):
    def wrapper():
        print("# potatoes #")
        func()
        print("~ salad ~")
    return wrapper



@bread
@ingredients
def sandwich(food = " --ham-- "):
    print(food)

sandwich()