package main

import (
	"bufio"
	"log"
	"os"
	"strings"
)

func filterBitStrings(report []string, pos int, operation string) []string {
	posCounts := make([]map[string]int, 12)

	row := 0
	for _, v := range report {
		res := strings.Split(v, "")

		for i := 11; i >= 0; i-- {
			if posCounts[i] == nil {
				posCounts[i] = make(map[string]int, 0)
			}

			posCounts[i][res[i]] += 1
		}
		row += 1
	}

	filteredSet := make([]string, 0)
	for _, v := range report {
		res := strings.Split(v, "")

		index := len(v) - 1 - pos

		matchChar := ""
		if operation == "o2" {
			matchChar = "1"
			if posCounts[index]["0"] > posCounts[index]["1"] {
				matchChar = "0"
			}
		}
		if operation == "co2" {
			matchChar = "0"
			if posCounts[index]["1"] < posCounts[index]["0"] {
				matchChar = "1"
			}
		}

		if matchChar == res[index] {
			filteredSet = append(filteredSet, v)
		}
	}
	return filteredSet
}

func main() {
	file, err := os.Open("../inputs/day_3_1_input.txt")
	//file, err := os.Open("../inputs/day_3_test.txt")

	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	reports := make([]string, 0)
	for scanner.Scan() {
		line := scanner.Text()
		reports = append(reports, line)
	}

	for i := 11; i >= 0; i-- {
		reports = filterBitStrings(reports, i, "co2")
		log.Printf("%v", reports)
	}
}
