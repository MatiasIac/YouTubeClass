
class Parent(object):
    x = 0

    def __init__(self):
        self.x = 10

    def parent_func(self):
        print self.x

class Child(Parent):

    def __init__(self):
        Parent.__init__(self)
        self.y = 10

    def show_parent(self):
        print self.parent_func()

c = Child()
c.show_parent()

p = Parent()