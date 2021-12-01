package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
)

func main() {
	file, err := os.Open("../inputs/day_1_1_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	m := make([]int64, 0)
	for scanner.Scan() {
		n, _ := strconv.ParseInt(scanner.Text(), 10, 64)
		m = append(m, n)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	a := m[0]
	count := 0

	for i := 1; i < len(m); i++ {
		b := m[i]
		if b > a {
			count += 1
		}
		a = b
	}

	log.Printf("Answer %v", count)
}
