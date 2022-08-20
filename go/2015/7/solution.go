package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var nodes = map[string]string{}
var text = []string{}

func main() {
	readInput()
	for !checkIfNumber(nodes["a"]) {
		// for i := 0; i < 400; i++ {
		proccesInput()
		proccesOpperations()
		standalone_numbers := getRoots()
		// fmt.Println(len(standalone_numbers))
		// fmt.Println(standalone_numbers)
		for _, standalone_number := range standalone_numbers {
			replace(standalone_number, nodes[standalone_number])
		}
		// proccesInput()
	}
	// fmt.Println(text[39])
	fmt.Println(nodes["a"])
	// for _, line := range text {
	// 	fmt.Println(line)
	// }

}

func proccesOpperations() {
	for i, opperation_raw := range text {
		// fmt.Println(opperation_raw)
		opperation := strings.Split(opperation_raw, " -> ")
		if strings.Contains(opperation[0], "AND") {
			opperation_parts := strings.Split(opperation[0], " AND ")
			if checkIfNumber(opperation_parts[0]) && checkIfNumber(opperation_parts[1]) {
				o1, _ := strconv.Atoi(opperation_parts[0])
				o2, _ := strconv.Atoi(opperation_parts[1])
				result := o1 & o2
				text[i] = strconv.Itoa(result) + " -> " + opperation[1]
				// fmt.Println(result)
			}
			// fmt.Println(opperation)
		}
		if strings.Contains(opperation[0], "OR") {
			opperation_parts := strings.Split(opperation[0], " OR ")
			if checkIfNumber(opperation_parts[0]) && checkIfNumber(opperation_parts[1]) {
				o1, _ := strconv.Atoi(opperation_parts[0])
				o2, _ := strconv.Atoi(opperation_parts[1])
				result := o1 | o2
				text[i] = strconv.Itoa(result) + " -> " + opperation[1]
				// fmt.Println(result)
			}
		}
		if strings.Contains(opperation[0], "LSHIFT") {
			opperation_parts := strings.Split(opperation[0], " LSHIFT ")
			if checkIfNumber(opperation_parts[0]) && checkIfNumber(opperation_parts[1]) {
				o1, _ := strconv.Atoi(opperation_parts[0])
				o2, _ := strconv.Atoi(opperation_parts[1])
				result := o1 << o2
				text[i] = strconv.Itoa(result) + " -> " + opperation[1]
				// fmt.Println(result)
			}
		}
		if strings.Contains(opperation[0], "RSHIFT") {
			opperation_parts := strings.Split(opperation[0], " RSHIFT ")
			if checkIfNumber(opperation_parts[0]) && checkIfNumber(opperation_parts[1]) {
				o1, _ := strconv.Atoi(opperation_parts[0])
				o2, _ := strconv.Atoi(opperation_parts[1])
				result := o1 >> o2
				text[i] = strconv.Itoa(result) + " -> " + opperation[1]
				// fmt.Println(result)
			}
		}
		if strings.Contains(opperation[0], "NOT") {
			opperation_parts := strings.Split(opperation[0], "NOT ")
			// fmt.Println(opperation_parts[1])
			if checkIfNumber(opperation_parts[1]) {
				o1, _ := strconv.Atoi(opperation_parts[1])
				result := ^o1 & 0xffff
				text[i] = strconv.Itoa(result) + " -> " + opperation[1]
				// fmt.Println(result)
			}
		}
	}
}

func replace(key string, value string) {
	for i, _ := range text {
		result := ""
		parts := strings.Split(text[i], " -> ")
		op_parts := strings.Split(parts[0], " ")
		for _, op_part := range op_parts {
			if op_part == key {
				result += value + " "
			} else {
				result += op_part + " "
			}
		}
		text[i] = result + "-> " + parts[1]
		// fmt.Println(text[i])
	}
}

func getRoots() []string {
	var roots = []string{}
	for _, node := range nodes {
		if len(strings.Split(node, " ")) < 2 {
			// fmt.Println()
			if checkIfNumber(node) {
				key, _ := mapkey(nodes, node)
				// fmt.Println(key + ":" + node)
				roots = append(roots, key)
			}
		}
	}
	return roots
}

func mapkey(m map[string]string, value string) (key string, ok bool) {
	for k, v := range m {
		if v == value {
			key = k
			ok = true
			return
		}
	}
	return
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

func proccesInput() {
	for _, opperation := range text {
		parts := strings.Split(opperation, " -> ")
		nodes[parts[1]] = parts[0]
	}
}

func checkIfNumber(number string) bool {
	_, err := strconv.Atoi(number)
	return err == nil
}
