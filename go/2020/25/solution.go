package main

import "fmt"

func main() {
	solution1(12092626, 4707356)
	// solution1(5764801, 17807724)
}

func solution1(pubKeyDoor int, pubKeyCard int) {
	loopSizeDoor := getLoopSize(7, pubKeyDoor)
	// loopSizeCard := getLoopSize(7, pubKeyCard)
	// fmt.Println(loopSizeDoor)
	// fmt.Println(loopSizeCard)
	fmt.Println(transform(pubKeyCard, loopSizeDoor))

}

func getLoopSize(subNr int, pubKey int) int {
	value := 1
	counter := 0
	for value != pubKey {
		value = value * subNr
		value = value % 20201227
		counter += 1
	}
	return counter
}

func transform(subNr int, loopSz int) int {
	value := 1
	for i := 0; i < loopSz; i++ {
		value = value * subNr
		value = value % 20201227
	}
	return value
}
