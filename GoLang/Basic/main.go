package main

import (
	"fmt"
)

func sumar(a, b int) int {
	return a + b
}

func prueba() (string, string) {
	return "hola", "mundo"
}

func main() {
	//fmt.Println(sumar(10, 20))
	a, b := prueba()
	fmt.Println(a, b)
}
