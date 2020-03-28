def swUno():
    return "Uno"

def swDos():
    return "Dos"

def swTres():
    return "Tres"

def swDefault():
    return "Valor por defecto"

def switch(arg):
    return {
        1: swUno,
        2: swDos,
        3: swTres
    }.get(arg, swDefault)

a = switch(1000)()
print a
