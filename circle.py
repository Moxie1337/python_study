class Circle:
    all_circles = []
    pi = 3.1415926
    def __init__(self, r = 1):
        self.radius = r
        self.__class__.all_circles.append(self)
        # print(self.__class__)

    def area(self):
        return self.__class__.pi * self.radius * self.radius

    @staticmethod
    def total_area_static():
        total = 0
        for c in Circle.all_circles:
            total = total + c.area()
        return total

    @classmethod # class method passed the class they belong to as their first parameter
    def total_area_class(cls):# cls = Circle
        total = 0
        for c in cls.all_circles:
            total = total + c.area()
        return total