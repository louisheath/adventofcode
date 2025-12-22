package main

func laboratories() int {
	manifold := readFile("7_input.txt")

	width := len(manifold[0])
	beams := make([]int, width)
	for i, ch := range manifold[0] {
		if ch == 'S' {
			beams[i] = 1
		}
	}

	dimensions := 1

	for i := 1; i < len(manifold); i++ {
		row := manifold[i]
		// go through all of the next digits
		// is a beam coming?
		//  is the path clear? continue the beam
		//  is there a splitter? split the beam
		//  assume splitters can't be next to each other
		for j := 0; j < width; j++ {
			if beams[j] == 0 {
				continue
			}
			if row[j] == '.' {
				continue
			}
			if row[j] == '^' {
				dimensions += beams[j]
				prev := j - 1
				if prev > -1 {
					beams[prev] += beams[j]
				}
				next := j + 1
				if next < width {
					beams[next] += beams[j]
				}
				beams[j] = 0
			}
		}
	}

	return dimensions
}
