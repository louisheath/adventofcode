package main

func printingDept() int {
	grid := readFile("4_input.txt")
	length := len(grid)
	width := len(grid[0])

	total := 0

	for i := 0; i < length; i++ {
		for j := 0; j < width; j++ {
			if string(grid[i][j]) != "@" {
				continue
			}
			neighbours := [][]int{
				{i - 1, j - 1},
				{i - 1, j},
				{i - 1, j + 1},
				{i, j - 1},
				{i, j + 1},
				{i + 1, j - 1},
				{i + 1, j},
				{i + 1, j + 1},
			}
			count := 0
			for _, n := range neighbours {
				x, y := n[0], n[1]
				if x == -1 || x == length || y == -1 || y == width {
					// out of bounds
					continue
				}
				if string(grid[x][y]) == "@" {
					count++
				}
			}
			if count < 4 {
				total++
			}
		}
	}

	return total
}
