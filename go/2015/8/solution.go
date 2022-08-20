package main

import (
	"bufio"
	"fmt"
	"os"
)

var text = []string{}

func main() {
	readInput()
	fmt.Println(countComplete() - countInterpreted())
}

func readInput() {
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
		text = append(text, result)

	}
}

func countComplete() int {
	count := 0
	for _, line := range text {
		count += len(line)
	}
	return count
}

func countInterpreted() int {
	count := 0
	for _, line := range text {
		skip := 0
		for i, char := range line {
			if string(char) != " " {
				if i != 0 && i != len(line)-1 {
					if skip != 0 {
						skip--
						// fmt.Println("Skipping " + string(char))
					} else {
						if string(char) == "\\" && (string(line[i+1]) == "\\" || string(line[i+1]) == "\"") {
							skip += 1
							count++
						} else if string(char) == "\\" {
							skip += 3
							count++
						} else {
							count++
						}
					}
				}
			}
			// fmt.Println(result)

		}
		// count += len(line)
	}
	return count
}
