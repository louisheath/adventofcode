package main

import (
	"log"
	"strconv"
	"strings"
)

func trashCompactor() int {
	input := readFile("6_input.txt")

	digits := [][]int{}
	for i := 0; i < len(input)-1; i++ {
		line := []int{}
		strs := strings.Split(input[i], " ")
		for _, s := range strs {
			if s != "" {
				digit, err := strconv.Atoi(s)
				if err != nil {
					log.Fatal(err)
				}
				line = append(line, digit)
			}
		}
		digits = append(digits, line)
	}

	total := 0

	operations := strings.Split(input[len(input)-1], " ")
	j := 0
	for _, operation := range operations {
		if operation == "" {
			continue
		}
		answer := 0
		if operation == "*" {
			answer = 1
		}
		for _, line := range digits {
			if operation == "*" {
				answer *= line[j]
			} else {
				answer += line[j]
			}
		}
		total += answer
		j++
	}

	return total
}
