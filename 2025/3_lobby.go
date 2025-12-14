package main

import (
	"log"
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

		firstDigit := -1
		firstDigitIndex := 0
		for i := 0; i < len(bank)-1; i++ {
			if digits[i] > firstDigit {
				firstDigit = digits[i]
				firstDigitIndex = i
			}
		}
		secondDigit := -1
		for i := firstDigitIndex + 1; i < len(bank); i++ {
			if digits[i] > secondDigit {
				secondDigit = digits[i]
			}
		}

		joltage := firstDigit*10 + secondDigit
		total += joltage
	}

	return total
}
