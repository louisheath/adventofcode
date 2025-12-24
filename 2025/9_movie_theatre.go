package main

import (
	"fmt"
	"image"
	"image/color"
	"image/png"
	"log"
	"math"
	"os"
	"strconv"
	"strings"
	"time"

	"github.com/davecgh/go-spew/spew"
)

const SHOULD_DRAW = true

func movieTheatre() int {
	input := readFile("9_input.txt")

	// Parse all tile coordinates into structs
	tiles := make([]*tile, len(input))
	height, width := 0, 0
	for i, line := range input {
		coords := strings.Split(line, ",")
		col, err := strconv.Atoi(coords[0])
		if err != nil {
			log.Fatal((err))
		}
		if col+2 > width {
			width = col + 2
		}
		row, err := strconv.Atoi(coords[1])
		if err != nil {
			log.Fatal((err))
		}
		if row+2 > height {
			height = row + 2
		}
		tiles[i] = &tile{row, col}
	}

	// Instantiate grid
	tileMap := make([][]bool, height)
	for i := range tileMap {
		tileMap[i] = make([]bool, width)
	}

	// Draw the borders onto the map
	fmt.Println("Drawing tile borders...")
	totalR, totalC := 0, 0
	for i := 0; i < len(tiles); i++ {
		tile := tiles[i]
		nextTile := tiles[(i+1)%len(tiles)]

		if tile.row == nextTile.row {
			start := min(tile.col, nextTile.col)
			end := max(tile.col, nextTile.col)
			for col := start; col <= end; col++ {
				tileMap[tile.row][col] = true
			}
		} else if tile.col == nextTile.col {
			start := min(tile.row, nextTile.row)
			end := max(tile.row, nextTile.row)
			for row := start; row <= end; row++ {
				tileMap[row][tile.col] = true
			}
		} else {
			spew.Dump(tile, nextTile)
			log.Fatal("expected col or row to equal")
		}

		totalR += tile.row
		totalC += tile.col
	}

	// Hope that the average red tile position is within
	avgRow := (totalR / len(tiles))
	// My test data set is a circle with a non-tiled middle
	avgRow -= height / 10
	avgCol := totalC / len(tiles)
	log.Printf("Centrepoint: (x %d y %d)\n", avgCol, avgRow)

	// Mark all tiles within the area
	// These map writes are really expensive.
	// I should store intervals of tile colour per row instead
	q := []tile{
		{avgRow, avgCol},
	}
	tileMap[avgRow][avgCol] = true

	i := 0
	t := time.Now()
	fmt.Println("Filling in tiles...")
	fmt.Printf(
		"i: %d, dur: %s, len(q): %d",
		i, time.Since(t).String(), len(q),
	)

	for len(q) > 0 {
		next := q[0]
		q = q[1:]

		neighbours := []tile{
			{next.row + 1, next.col},
			{next.row - 1, next.col},
			{next.row, next.col + 1},
			{next.row, next.col - 1},
		}
		for _, n := range neighbours {
			// is it within bounds?
			if n.row < 0 || n.col < 0 {
				continue
			}
			if n.row >= height || n.col >= width {
				continue
			}
			// is it already a tile? skip
			if tileMap[n.row][n.col] {
				continue
			}
			// queue it, mark it as a tile
			q = append(q, n)
			tileMap[n.row][n.col] = true
		}
		i++
		if i%1000 == 0 {
			fmt.Printf(
				"\ri: %d, dur: %s, len(q): %d",
				i, time.Since(t).String(), len(q),
			)
		}
	}
	fmt.Printf("\n")

	var im *image.Gray
	if SHOULD_DRAW {
		im = image.NewGray(image.Rectangle{Max: image.Point{X: width, Y: height}})
		fmt.Println("Setting white background")
		for i := range im.Pix {
			im.Pix[i] = 255 // Set a white background
		}
		fmt.Println("Drawing tiles")
		for y, row := range tileMap {
			for x := 0; x < width; x++ {
				if row[x] {
					im.Set(x, y, color.Black)
				}
			}
		}
	}

	fmt.Println("Calculating largest rectangle")
	largestArea := math.MinInt
	var x, y, h, w int
	for i, tile1 := range tiles {
	T:
		for j, tile2 := range tiles {
			if i == j {
				// avoid comparing the same two tiles twice
				break
			}

			// tile1 and tile2 form the borders, and so
			// are within the area. check the other 2x corners
			if !tileMap[tile1.row][tile2.col] {
				continue
			}
			if !tileMap[tile2.row][tile1.col] {
				continue
			}

			// check the area
			height := abs(tile2.row-tile1.row) + 1
			width := abs(tile2.col-tile1.col) + 1
			area := height * width
			if area <= largestArea {
				continue
			}

			// check that rectangle doesn't contain non-tile areas
			startX := min(tile1.col, tile2.col)
			startY := min(tile1.row, tile2.row)

			for row := startY; row < startY+height; row++ {
				// top edge
				if !tileMap[row][startX] {
					continue T
				}
				// bottom edge
				if !tileMap[row][startX+width-1] {
					continue T
				}
			}
			for col := startX; col < startX+width; col++ {
				// left edge
				if !tileMap[startY][col] {
					continue T
				}
				// right edge
				if !tileMap[startY+height-1][col] {
					continue T
				}
			}

			largestArea = area
			h, w = height, width
			x, y = startX, startY
		}
	}

	spew.Dump(x, y, h, w)

	if SHOULD_DRAW {
		fmt.Println("Drawing largest rectangle")
		for row := y; row < y+h; row++ {
			for col := x; col < x+w; col++ {
				im.Set(col, row, color.Gray16{0x6666}) // grey
			}
		}

		f, err := os.Create("9_tiles.png")
		if err != nil {
			log.Fatal(err)
		}
		defer f.Close() // Ensure the file is closed at the end

		fmt.Println("Writing image file")
		if err := png.Encode(f, im); err != nil {
			log.Fatal(err)
		}
	}

	return largestArea // 1452422268
}

type tile struct {
	row, col int
}

func abs(x int) int {
	if x < 0 {
		return -1 * x
	}
	return x
}
