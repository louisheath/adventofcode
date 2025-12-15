package main

import (
	"log"
	"strconv"
	"strings"
)

func cafeteria() int {
	input := readFile("5_input.txt")

	ranges := []idRange{}
	total := 0
	processingRanges := true

	for _, line := range input {
		if line == "" {
			// We've processed all fresh ingredient ranges
			processingRanges = false
			continue
		}

		if processingRanges {
			s := strings.Split(line, "-")
			start, err := strconv.Atoi(s[0])
			if err != nil {
				log.Fatal(err)
			}
			end, err := strconv.Atoi(s[1])
			if err != nil {
				log.Fatal(err)
			}
			ranges = append(ranges, idRange{start, end})
			continue
		}

		ingredient, err := strconv.Atoi(line)
		if err != nil {
			log.Fatal(err)
		}

		for _, r := range ranges {
			if ingredient >= r.start && ingredient <= r.end {
				total++
				break
			}
		}
	}

	return total
}

type idRange struct {
	start int
	end   int
}
