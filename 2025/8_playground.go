package main

import (
	"log"
	"math"
	"sort"
	"strconv"
	"strings"
)

const MAX_CONNS = 1000

func playground() int {
	boxes := readFile("8_input.txt")

	// Parse all string boxes into structs
	junctionBoxes := make([]*junctionBox, len(boxes))
	for i, line := range boxes {
		coords := strings.Split(line, ",")
		x, err := strconv.Atoi(coords[0])
		if err != nil {
			log.Fatal((err))
		}
		y, err := strconv.Atoi(coords[1])
		if err != nil {
			log.Fatal((err))
		}
		z, err := strconv.Atoi(coords[2])
		if err != nil {
			log.Fatal((err))
		}
		junctionBoxes[i] = &junctionBox{x, y, z}
	}

	// Calculate distances between all boxes. O(n^2)
	possibleConns := []connection{}
	for i, box1 := range junctionBoxes {
		for j, box2 := range junctionBoxes {
			if i == j {
				// rather than compare everything twice, break halfway
				break
			}
			distance := box1.dist(box2)
			possibleConns = append(possibleConns, connection{
				distance, box1, box2,
			})
		}
	}

	// O(nlogn). Don't bother with binary search inserts
	sort.Slice(possibleConns, func(i, j int) bool {
		c1, c2 := possibleConns[i], possibleConns[j]
		return c1.distance < c2.distance
	})

	// Build graph of connected closest junction boxes
	graph := map[*junctionBox][]*junctionBox{}
	var lastConn connection
	for i := 0; len(graph) < len(junctionBoxes); i++ {
		conn := possibleConns[i]

		bs1 := graph[conn.a]
		bs1 = append(bs1, conn.b)
		graph[conn.a] = bs1

		bs2 := graph[conn.b]
		bs2 = append(bs2, conn.a)
		graph[conn.b] = bs2

		lastConn = conn
	}

	return lastConn.a.x * lastConn.b.x
}

type junctionBox struct {
	x, y, z int
}

func (b *junctionBox) dist(a *junctionBox) float64 {
	x := b.x - a.x
	y := b.y - a.y
	z := b.z - a.z
	return math.Sqrt(float64(x*x + y*y + z*z))
}

type connection struct {
	distance float64
	a, b     *junctionBox
}
