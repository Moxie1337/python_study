import circle

def print_circles():
    for c in circle.Circle.all_circles:
        print(c)
    print()

c1 = circle.Circle(1)

# print_circles()
# print(c1)
c2 = circle.Circle(2)
# print_circles()

res = circle.Circle.total_area_static()

print(res)

c2.radius = 3

res = circle.Circle.total_area_class()

print(res)