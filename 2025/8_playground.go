package main

import "math"

func playground() int {
	_ = readFile("8_input.txt")

	/*
		I need to find the two boxes closest together and join them into the same circuit
		I need to do this 1000 times
		I then need to take the three largest circuits and multiply together the number of boxes in each

		I need a data structure to hold shortest distances
		and a data structure to hold circuits
		both could be graphs

		Shortest distances
		O(n2), find the distance between all boxes using pythagoras, create a fully connected graph
		Also maintain a sorted list of these connections and their distances so that we can easily
		pull the shortest. Actually, maybe we only need the sorted list.

		When two boxes are connected, we'll join them in an adjacency list
		After connecting 1000 boxes, we can explore the adjacent list graph to find the number of created circuits and their sizes
	*/

	// loop 1 parse all string boxes into structs

	// loop 2 double for-each, calculate distances, append to slice

	// loop 3 sort the slice O(nlogn). we've already done an O(n^2). don't bother with binary search insert

	// loop 4 iterate through the first 1000, build graph

	// loop 5 explore the graph, find the sizes of each circuit

	return 1
}

type connection struct {
	distance float64
	i        int
	j        int
}

func dist(a, b, c, d, e, f int) float64 {
	x := a - d
	y := b - e
	z := c - f
	return math.Sqrt(float64(x*x + y*y + z*z))
}
