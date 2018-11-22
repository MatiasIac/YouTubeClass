function sumar(a, b) {
    if (typeof(a) === 'string') {
        return null;
    }

    if (typeof(b) === 'string') {
        return null;
    }

    return a + b;
}

//Test positivos
console.log(sumar(10, 20) == 30)
console.log(sumar(-10, 20) == 10)

//Test negativos
console.log(sumar('a', 10))
console.log(sumar(10, 'a'))