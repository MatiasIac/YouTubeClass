
class MyEx(Exception):
    def __init__(self, valor):
        self.value = valor

    def __str__(self):
        return repr(self.value)

class MyErrorClass(object):

    def __init__(self):
        self.message = "Message"

    def throw_errors(self):
        #raise ArithmeticError('No se puede divir por cero')
        #raise Exception('Un error', 'Otro argumento')
        #print "no hay error"
        raise MyEx('Error personalizado')

myErr = MyErrorClass()

try:
    myErr.throw_errors()
except MyEx as m:
    print m
except ArithmeticError:
    print "Error aritmetico"
except Exception as e:
    #print e
    #print type(e)
    #print e.args
    a, b = e.args
    print a
    print b
else:
    print "Todo ok"
finally:
    print "Al final"

