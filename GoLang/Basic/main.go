package main

import (
	"fmt"
)

func getFunc() func() {
	return func() {
		fmt.Println("Hola Mundo")
	}
}

func setFunc(f func()) {
	f()
}

func main() {
	setFunc(func() {
		fmt.Println("Hola mundo!")
	})
}