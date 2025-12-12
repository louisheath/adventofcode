package main

import (
	"log"
	"strconv"
)

func secretEntrance() int {
	rotations := readFile("1_input.txt")

	dialPosition := 50
	password := 0

	for _, rotation := range rotations {
		direction := rotation[:1]
		distance, err := strconv.Atoi(rotation[1:])
		if err != nil {
			log.Fatal(err)
		}

		if direction == "R" {
			dialPosition += distance
		} else {
			dialPosition -= distance
		}
		dialPosition = mod(dialPosition, 100)

		if dialPosition == 0 {
			password++
		}
	}

	return password
}

func mod(x, y int) int {
	return (x%y + y) % y
}
