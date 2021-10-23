
class Point:
    # El argumento self es una referencia al objeto sobre el que se invoca el metodo
    def reset(self):
        self.x = 0
        self.y = 0

p = Point()
p.reset()
print(p.x, p.y)

""" This is not really a good programming practice, but it can help
    to cement your understanding of the self argument."""
p2 = Point()
Point.reset(p2)
print(p2.x, p2.y)