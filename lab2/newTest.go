package main

import "fmt"

var positiveCounter1 int = 0
var ifCounter1 int = 0
var positiveCounter0 int = 0
var ifCounter0 int = 0

func main() {
        var i int = 0
        ifCounter0++
        if i++; 1 == 1 {
                positiveCounter0++
                i++
        } else if 1 == 0 {
                i--
        } else {
                fmt.Printf("%d", i)
        }
        ifCounter1++
        if true {
                positiveCounter1++

        }
        fmt.Printf("if #%d all call is %d \n if #%d positive block all call is %d", 0, ifCounter0, 0, positiveCounter0)
        fmt.Printf("if #%d all call is %d \n if #%d positive block all call is %d", 1, ifCounter1, 1, positiveCounter1)
}