package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("../inputs/day_2_1_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	x := 0
	y := 0
	aim := 0

	for scanner.Scan() {
		line := scanner.Text()
		res := strings.Split(line, " ")
		op := res[0]
		amt, _ := strconv.Atoi(res[1])

		if op == "forward" {
			x += amt
			y += aim * amt
		} else if op == "up" {
			aim -= amt
		} else if op == "down" {
			aim += amt
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	log.Printf("Day 2 Part 2 Answer %v ", x*y)
}
