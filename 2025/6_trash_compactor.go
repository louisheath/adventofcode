package main

import (
	"log"
	"math"
	"strconv"
	"strings"
)

func trashCompactor() int {
	input := readFile("6_input.txt")

	// operations left to right
	operations := []string{}
	for _, op := range strings.Split(input[len(input)-1], " ") {
		if op == "" {
			continue
		}
		operations = append(operations, op)
	}

	numberGroups := make([][]int, len(operations))
	groupNumber := 0

	// for every column of characters
	for i := 0; i < len(input[0]); i++ {
		number := 0
		allAreSpaces := true
		// build the number from bottom to top
		pow := 0
		for j := 0; j <= len(input)-2; j++ {
			row := len(input) - 2 - j
			char := string(input[row][i])
			if char == " " {
				continue
			}
			allAreSpaces = false
			digit, err := strconv.Atoi(char)
			if err != nil {
				log.Fatal(err)
			}
			number += digit * int(math.Pow(10, float64(pow)))
			pow++
		}
		if allAreSpaces {
			groupNumber++
		} else {
			group := numberGroups[groupNumber]
			group = append(group, number)
			numberGroups[groupNumber] = group
		}
	}

	total := 0

	for i, op := range operations {
		answer := 0
		if op == "*" {
			answer = 1
		}
		numbers := numberGroups[i]
		for _, num := range numbers {
			if op == "*" {
				answer *= num
			} else {
				answer += num
			}
		}
		total += answer
	}

	return total
}
