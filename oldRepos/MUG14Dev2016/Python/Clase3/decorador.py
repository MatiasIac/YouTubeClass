
class MiValidadorParametros(object):

    def __init__(self, func):
        self.target_func = func

    def __call__(self, arg1, arg2):
        if arg1 < 10:
            print 'El valor 1 tiene que ser mayor o igual a 10'
        else:
            return self.target_func(arg1, arg2)


@MiValidadorParametros
def SumarValor(valor, valor2):
    return valor + valor2

print SumarValor(5, 20)