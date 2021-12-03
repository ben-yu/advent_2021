package main

import (
	"bufio"
	"log"
	"os"
	"strings"
)

func main() {
	file, err := os.Open("../inputs/day_3_1_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	//gamma := 0
	//epsilon := 0

	posCounts := make([]map[string]int, 12)

	row := 0
	for scanner.Scan() {
		line := scanner.Text()
		res := strings.Split(line, "")
		for i := 0; i < len(res); i++ {
			if posCounts[i] == nil {
				posCounts[i] = make(map[string]int, 0)
			}

			posCounts[i][res[i]] += 1
		}
		row += 1
	}

	gamma := ""
	for i := 0; i < 12; i++ {
		if posCounts[i]["0"] > posCounts[i]["1"] {
			gamma = "0" + gamma
		} else {
			gamma = "1" + gamma
		}
	}
	epsilon := ""
	for i := 0; i < 12; i++ {
		if posCounts[i]["0"] < posCounts[i]["1"] {
			epsilon = "0" + epsilon
		} else {
			epsilon = "1" + epsilon
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	log.Printf("%v", gamma)
	log.Printf("%v", epsilon)

}
