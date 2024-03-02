package main

import "fmt"
func main() {
	var i int = 0
	if i++; (1 == 1) {
		i++
	} else if (1 == 0){
		i--
	} else {
		fmt.Printf("%d", i)
	}
	if true {
		
	}
}