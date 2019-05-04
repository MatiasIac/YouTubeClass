#include <stdio.h>

int sumar(int a, int b) {
    int r = a + b;
    return r;
}

int main() {
    //int resultado = sumar(20, 30);
    //printf("Resultado: %d", resultado);

    int a = 30;
    int *puntero;

    puntero = &a;
    
    printf("valor de a: %d\n", a);
    printf("direccion de a: %x\n", &a);
    printf("direccion de puntero: %x\n", puntero);
    printf("valor de puntero: %d\n", *puntero);

    return 0;
}