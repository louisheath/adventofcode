package main

import (
	"log"
	"math"
	"strconv"
	"strings"
)

func movieTheatre() int {
	input := readFile("9_input.txt")

	// Parse all string boxes into structs
	tiles := make([]*redTile, len(input))
	for i, line := range input {
		coords := strings.Split(line, ",")
		col, err := strconv.Atoi(coords[0])
		if err != nil {
			log.Fatal((err))
		}
		row, err := strconv.Atoi(coords[1])
		if err != nil {
			log.Fatal((err))
		}
		tiles[i] = &redTile{row, col}
	}

	largestArea := math.MinInt

	for i, tile1 := range tiles {
		for j, tile2 := range tiles {
			if i == j {
				// avoid comparing the same two tiles twice
				break
			}
			height := abs(tile2.row - tile1.row + 1)
			width := abs(tile2.col - tile1.col + 1)
			area := height * width
			if area > largestArea {
				largestArea = area
			}
		}
	}

	return largestArea
}

type redTile struct {
	row, col int
}

func abs(x int) int {
	if x < 0 {
		return -1 * x
	}
	return x
}
