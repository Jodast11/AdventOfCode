package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var instructions = [300][5]int{{}}
var lights = [1000][1000]int{{}}

func main() {
	readInput()
	// fmt.Println(instructions)
	applyOpperations()
	// fmt.Println(lights)
	fmt.Println(getLightLevel())

}

func getLightLevel() int {
	counter := 0
	for x := 0; x < 1000; x++ {
		for y := 0; y < 1000; y++ {
			counter += lights[x][y]
		}
	}
	return counter
}

func applyOpperations() {
	for _, instruction := range instructions {
		if instruction[0] == 0 {
			switchOff(instruction[1], instruction[2], instruction[3], instruction[4])
		}
		if instruction[0] == 1 {
			switchOn(instruction[1], instruction[2], instruction[3], instruction[4])
		}
		if instruction[0] == 2 {
			toggle(instruction[1], instruction[2], instruction[3], instruction[4])
		}
	}
}

func switchOff(fromX int, fromY int, toX int, toY int) {
	for x := 0; x < 1000; x++ {
		for y := 0; y < 1000; y++ {
			if fromX <= x && toX >= x {
				if fromY <= y && toY >= y {
					if lights[x][y] > 0 {
						lights[x][y] -= 1
					}
				}
			}
		}
	}
}

func switchOn(fromX int, fromY int, toX int, toY int) {
	for x := 0; x < 1000; x++ {
		for y := 0; y < 1000; y++ {
			if fromX <= x && toX >= x {
				if fromY <= y && toY >= y {
					lights[x][y] += 1
				}
			}
		}
	}
}

func toggle(fromX int, fromY int, toX int, toY int) {
	for x := 0; x < 1000; x++ {
		for y := 0; y < 1000; y++ {
			if fromX <= x && toX >= x {
				if fromY <= y && toY >= y {
					lights[x][y] += 2
				}
			}
		}
	}
}

func readInput() {
	i := 0
	filePtr, err := os.Open("input.txt")
	if err != nil {
		fmt.Println(err)
	}

	myScanner := bufio.NewScanner(filePtr)

	for {
		result_raw := myScanner.Scan()
		if !result_raw {
			err = myScanner.Err()
			if err == nil {
				// fmt.Println("Reached to the end of file")
				break
			} else {
				fmt.Println(err)
				break
			}
		}
		result := myScanner.Text()
		// fmt.Println(result)
		if strings.Contains(result, "off") {
			instructions[i][0] = 0
			result = strings.Replace(result, "turn off ", "", -1)
		}
		if strings.Contains(result, "on") {
			instructions[i][0] = 1
			result = strings.Replace(result, "turn on ", "", -1)
		}
		if strings.Contains(result, "toggle") {
			instructions[i][0] = 2
			result = strings.Replace(result, "toggle ", "", -1)
		}
		results := strings.Split(result, " ")
		instructions[i][1], _ = strconv.Atoi(strings.Split(results[0], ",")[0])
		instructions[i][2], _ = strconv.Atoi(strings.Split(results[0], ",")[1])
		instructions[i][3], _ = strconv.Atoi(strings.Split(results[2], ",")[0])
		instructions[i][4], _ = strconv.Atoi(strings.Split(results[2], ",")[1])
		i++

	}
}
