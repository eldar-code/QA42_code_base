from core.shapes import Rectangle, Circle, get_shape_area

r1 = Rectangle()
r1.length = 10
r1.width = 3
print(r1.get_area())

c1 = Circle()
c1.radius = 2.5
print(c1.get_area())

get_shape_area(r1)
get_shape_area(c1)
# get_shape_area("")
