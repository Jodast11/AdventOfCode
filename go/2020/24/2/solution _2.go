package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	tiles := getTiles()
	// fmt.Println(tiles)
	// fmt.Println(countAdjacentBlack("0|0", tiles))
	for i := 0; i < 100; i++ {
		tiles = applyOpperations(tiles)
		fmt.Println(countBlacks(tiles))
	}
}

func countBlacks(tiles map[string]int) int {
	counter := 0
	for key := range tiles {
		// fmt.Println(val)
		if tiles[key] == 1 {
			counter++
		}
	}
	return counter
}

func applyOpperations(tiles_old map[string]int) map[string]int {
	res := tiles_old
	rule1Res := applyRule1(tiles_old)
	rule2Res := applyRule2(tiles_old)
	for change := range rule1Res {
		res[change] = 0
	}
	for change := range rule2Res {
		res[change] = 1
	}
	return res
}

func applyRule2(tiles_old map[string]int) map[string]int {
	tiles_new := map[string]int{}
	allWhiteCoords := []string{}
	for key := range tiles_old {
		if tiles_old[key] == 1 {
			recentWhiteCoords := getAdjacentWhiteCoords(key, tiles_old)
			allWhiteCoords = append(allWhiteCoords, recentWhiteCoords...)
		}
	}
	for _, coord := range allWhiteCoords {
		if countAdjacentBlack(coord, tiles_old) == 2 {
			tiles_new[coord] = 1
		}
	}
	return tiles_new
}

func getAdjacentWhiteCoords(origin string, tiles map[string]int) []string {
	allAdjacent := getAdjacentCoords(origin)
	whiteAdjacent := []string{}
	for _, key := range allAdjacent {
		if tiles[key] == 0 {
			whiteAdjacent = append(whiteAdjacent, key)
		}
	}
	return whiteAdjacent
}

func applyRule1(tiles_old map[string]int) map[string]int {
	tiles_new := map[string]int{}
	for key := range tiles_old {
		if tiles_old[key] == 1 {
			nrAdjacent := countAdjacentBlack(key, tiles_old)
			if nrAdjacent == 0 || nrAdjacent > 2 {
				tiles_new[key] = 0
			}
		}
	}
	return tiles_new
}

func countAdjacentBlack(origin string, tiles map[string]int) int {
	adjacent := getAdjacentCoords(origin)
	// fmt.Println(adjacent)
	counter := 0
	for _, cord := range adjacent {
		val, ok := tiles[cord]
		if ok {
			if val == 1 {
				counter++
			}
		}
	}
	return counter
}

func getAdjacentCoords(origin string) []string {
	adjacent := []string{}
	coords := strings.Split(origin, "|")
	posXOrigin, _ := strconv.Atoi(coords[0])
	posYOrigin, _ := strconv.Atoi(coords[1])

	adjacent = append(adjacent, (strconv.Itoa(posXOrigin+1) + "|" + strconv.Itoa(posYOrigin+1)))
	adjacent = append(adjacent, (strconv.Itoa(posXOrigin+0) + "|" + strconv.Itoa(posYOrigin+1)))
	adjacent = append(adjacent, (strconv.Itoa(posXOrigin-1) + "|" + strconv.Itoa(posYOrigin+0)))
	adjacent = append(adjacent, (strconv.Itoa(posXOrigin-1) + "|" + strconv.Itoa(posYOrigin-1)))
	adjacent = append(adjacent, (strconv.Itoa(posXOrigin+0) + "|" + strconv.Itoa(posYOrigin-1)))
	adjacent = append(adjacent, (strconv.Itoa(posXOrigin+1) + "|" + strconv.Itoa(posYOrigin+0)))

	return adjacent
}

func getTiles() map[string]int {
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
	}
	return tiles
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
