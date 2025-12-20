package main

func laboratories() int {
	manifold := readFile("7_input.txt")

	width := len(manifold[0])
	beams := make([]bool, width)
	for i, ch := range manifold[0] {
		if ch == 'S' {
			beams[i] = true
		}
	}

	splits := 0

	for i := 1; i < len(manifold); i++ {
		row := manifold[i]
		// go through all of the next digits
		// is a beam coming?
		//  is the path clear? continue the beam
		//  is there a splitter? split the beam
		//  assume splitters can't be next to each other
		for j := 0; j < width; j++ {
			if !beams[j] {
				continue
			}
			if row[j] == '.' {
				continue
			}
			if row[j] == '^' {
				splits++
				beams[j] = false
				prev := j - 1
				if prev > -1 {
					beams[prev] = true
				}
				next := j + 1
				if next < width {
					beams[next] = true
				}
			}
		}
	}

	return splits
}
