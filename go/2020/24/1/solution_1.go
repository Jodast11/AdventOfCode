package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	tiles := map[string]int{}
	directions := readInput("input.txt")
	for _, direction := range directions {
		posX, posY := getLocation(direction)
		posStr := strconv.Itoa(posX) + "|" + strconv.Itoa(posY)
		val, ok := tiles[posStr]
		if !ok {
			tiles[posStr] = 1
		} else {
			if val == 0 {
				tiles[posStr] = 1
			} else {
				tiles[posStr] = 0
			}
		}
		// fmt.Println(posStr)

	}
	// fmt.Println(tiles)
	counter := 0
	for key := range tiles {
		// fmt.Println(val)
		if tiles[key] == 1 {
			counter++
		}
	}
	fmt.Println(counter)
}

func getLocation(direction string) (int, int) {
	xPos := 0
	yPos := 0
	posInString := 0
	for posInString < len(direction) {
		if string(direction[posInString]) == "e" {
			yPos++
			posInString++
			// fmt.Println("e")
			continue
		}
		if string(direction[posInString]) == "w" {
			yPos--
			posInString++
			// fmt.Println("w")
			continue
		}
		if string(direction[posInString]) == "n" {
			if string(direction[posInString+1]) == "e" {
				xPos++
				yPos++
				posInString += 2
				// fmt.Println("ne")
				continue
			}
			if string(direction[posInString+1]) == "w" {
				xPos++
				posInString += 2
				// fmt.Println("nw")
				continue
			}
		}
		if string(direction[posInString]) == "s" {
			if string(direction[posInString+1]) == "e" {
				xPos--
				posInString += 2
				// fmt.Println("se")
				continue
			}
			if string(direction[posInString+1]) == "w" {
				xPos--
				yPos--
				posInString += 2
				// fmt.Println("sw")
				continue
			}

		}
		// fmt.Println(posInString)
	}
	return xPos, yPos
}

func readInput(filePath string) []string {

	page := []string{}

	filePtr, err := os.Open(filePath)
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
		page = append(page, result)
	}
	return page

}
