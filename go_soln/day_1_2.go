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
	m := make([]int, 0)
	for scanner.Scan() {
		n, _ := strconv.ParseInt(scanner.Text(), 10, 64)
		m = append(m, int(n))
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	a := m[0]
	b := m[1]
	count := 0
	prevSum := 0
	curSum := 0

	for i := 2; i < len(m); i++ {
		c := m[i]
		curSum = a + b + c
		if curSum > prevSum {
			count += 1
		}
		prevSum = curSum
		a = b
		b = c
	}

	log.Printf("Answer %v", count-1)
}
