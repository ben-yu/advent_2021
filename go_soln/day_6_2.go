package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("../inputs/day_6_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	m := make([]int, 0)

	// Count by days 📊
	dayCounts := make([]int, 9)
	for scanner.Scan() {
		line := strings.Split(scanner.Text(), ",")
		for _, v := range line {
			n, _ := strconv.ParseInt(v, 10, 64)
			m = append(m, int(n))
			dayCounts[int(n)] += 1
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	numDays := 256

	for i := 1; i <= numDays; i++ {
		newSpawn := dayCounts[0]
		dayCounts = dayCounts[1:]               // Shift
		dayCounts[6] += newSpawn                // Old fish
		dayCounts = append(dayCounts, newSpawn) // new fish
	}

	sum := 0
	for _, v := range dayCounts {
		sum += v
	}
	log.Printf("Answer %v", sum)
}
