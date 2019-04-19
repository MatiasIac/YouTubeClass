#include <stdio.h>

int sumar(int a, int b) {
    int r = a + b;
    return r;
}

int main() {
    int resultado = sumar(20, 30);
    printf("Resultado: %d", resultado);

    return 0;
}