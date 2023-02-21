from shape import Shape, Circle

# c = Circle(1)

# c.move(3, 4)

# print(c.x, c.y)

class P:
    z = "Hello"
    def set_p(self):
        self.x = "Class p"
    def print_p(self):
        print(self.x)

class C(P):
    def set_c(self):
        self.x = "Class c"
    def print_c(self):
        print(self.x)

c = C()
c.set_p()
c.print_p()
c.print_c()

c.set_c()
c.print_p()
c.print_c()

