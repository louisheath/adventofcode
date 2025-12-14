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

		step := -1
		if direction == "R" {
			step = 1
		}

		for i := 0; i < distance; i++ {
			dialPosition = mod(dialPosition+step, 100)

			if dialPosition == 0 {
				password++
			}
		}
	}

	return password
}

func mod(x, y int) int {
	return (x%y + y) % y
}
