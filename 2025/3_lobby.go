package main

import (
	"log"
	"math"
	"strconv"
)

func lobby() int {
	file := readFile("3_input.txt")

	total := 0

	for _, bank := range file {
		digits := make([]int, len(bank))
		for i := 0; i < len(bank); i++ {
			digit, err := strconv.Atoi(string(bank[i]))
			if err != nil {
				log.Fatal(err)
			}
			digits[i] = digit
		}

		joltage := 0
		startIndex := 0

		for i := 11; i >= 0; i-- {
			highest := -1
			indexOfHighest := 0

			for j := startIndex; j < len(bank)-i; j++ {
				if digits[j] > highest {
					highest = digits[j]
					indexOfHighest = j
				}
			}

			joltage += highest * int(math.Pow(10, float64(i)))
			startIndex = indexOfHighest + 1
		}

		total += joltage
	}

	return total
}
