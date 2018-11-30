
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

--escribir("prueba")
--ejecutor(escribir, "otra prueba")

local f = Retornar()
f("Otra prueba mas")