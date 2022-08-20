package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	// solution1()
	solution2()
	// fmt.Println(checkRule2("aaa"))

}

func solution2() {
	validStrings := 0

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
				fmt.Println("Reached to the end of file")
				break
			} else {
				fmt.Println(err)
				break
			}
		}
		result := myScanner.Text()

		if checkRule1(result) && checkRule2(result) {
			validStrings++
		}

	}

	fmt.Println(validStrings)
}

func checkRule1(input string) bool {
	for i, _ := range input {
		if len(input) > i+2 {
			pair := input[i : i+2]
			// fmt.Println(pair)
			if strings.Contains(input[i+2:], pair) {
				return true
			}
		}
	}
	return false
}

func checkRule2(input string) bool {
	for i, _ := range input {
		if len(input) > i+2 {
			if input[i] == input[i+2] {
				return true
			}
		}
	}
	return false
}

func solution1() {
	validStrings := 0

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
				fmt.Println("Reached to the end of file")
				break
			} else {
				fmt.Println(err)
				break
			}
		}
		result := myScanner.Text()

		// fmt.Println(result)
		if countVowels(result) > 2 && checkDoubles(result) && checkForbidden(result) {
			validStrings++
		}
	}

	fmt.Println(validStrings)
}

func checkForbidden(input string) bool {
	if strings.Contains(input, "ab") || strings.Contains(input, "cd") || strings.Contains(input, "pq") || strings.Contains(input, "xy") {
		return false
	}
	return true
}

func checkDoubles(input string) bool {
	lastChar := ""
	for _, character := range input {
		if string(character) == lastChar {
			return true
		}
		lastChar = string(character)
	}
	return false
}

func countVowels(input string) int {
	vowelsCounter := 0
	for _, character := range input {
		if string(character) == "a" || string(character) == "e" || string(character) == "i" || string(character) == "o" || string(character) == "u" {
			vowelsCounter++
		}
	}
	return vowelsCounter
}
