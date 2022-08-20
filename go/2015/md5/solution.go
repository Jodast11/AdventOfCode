package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"strconv"
	"strings"
	"time"
)

func main() {
	start := time.Now()
	key := "bgvyzdsv"
	i := 0
	for {
		data_str := key + strconv.Itoa(i)
		data := []byte(data_str)
		output_bytes := md5.Sum(data)
		output := hex.EncodeToString(output_bytes[:])
		if strings.Contains(output[:6], "000000") {
			fmt.Println(output)
			fmt.Println(i)
			break
		}
		i++
	}
	fmt.Println(time.Since(start))
}
