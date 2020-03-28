
class My_Class(object):

    x = 10

    def __init__(self):
        self.x = 20
        print "My_Class esta inicializada"

    def sum_custom(self, val1):
        return self.x + val1

    def show_numbers(self):
        print __name__
