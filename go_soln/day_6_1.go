package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
	"sync"
	"sync/atomic"
)

var spawnCounter int64

func spawn(age int, daysLeft int, wg *sync.WaitGroup) {
	for i := 1; i <= daysLeft; i++ {
		if age == 0 {
			// call a new spawn
			wg.Add(1)
			go func(i int) {
				defer wg.Done()
				spawn(7, daysLeft-i-1, wg)
				// increment global counter
				atomic.AddInt64(&spawnCounter, 1)
				//fmt.Printf("%v\n", spawnCounter)
			}(i)
			age = 6 + 1
		}
		age -= 1
	}
}

func main() {
	file, err := os.Open("../inputs/day_6_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	m := make([]int, 0)
	for scanner.Scan() {
		line := strings.Split(scanner.Text(), ",")
		for _, v := range line {
			n, _ := strconv.ParseInt(v, 10, 64)
			m = append(m, int(n))
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	spawnCounter += int64(len(m))

	var wg sync.WaitGroup
	for _, v := range m {
		wg.Add(1)
		go func(v int) {
			defer wg.Done()
			spawn(v, 80, &wg)
		}(v)
	}

	wg.Wait()
	log.Printf("Answer %v", spawnCounter)
}
