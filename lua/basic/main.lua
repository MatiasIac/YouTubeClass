function_sumar = require('librerias')

function ejecutor(f, str)
    f(str)
end

function escribir(str)
    print(str)
end

function Retornar()
    return function (str)
        print(str)
    end
end

print(function_sumar(10, 20))

--escribir("prueba")
--ejecutor(escribir, "otra prueba")

--local f = Retornar()
--f("Otra prueba mas")