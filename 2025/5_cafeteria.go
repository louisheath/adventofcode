package main

import (
	"log"
	"sort"
	"strconv"
	"strings"
)

func cafeteria() int {
	input := readFile("5_input.txt")

	ranges := []*idRange{}

	for _, line := range input {
		if line == "" {
			// We've processed all fresh ingredient ranges
			break
		}
		s := strings.Split(line, "-")
		start, err := strconv.Atoi(s[0])
		if err != nil {
			log.Fatal(err)
		}
		end, err := strconv.Atoi(s[1])
		if err != nil {
			log.Fatal(err)
		}
		ranges = append(ranges, &idRange{start, end})
	}

	sort.Slice(ranges, func(i, j int) bool {
		ri, rj := ranges[i], ranges[j]
		if ri.start < rj.start {
			return true
		}
		if ri.start == rj.start {
			if ri.end < rj.end {
				return true
			}
		}
		return false
	})

	// merge overlapping intervals
	currIndex := 0

	for i := 1; i < len(ranges); i++ {
		curr := ranges[currIndex]
		next := ranges[i]
		// we know that next.start >= curr.start because of the sort

		if next.start > curr.end {
			currIndex++
			ranges[currIndex] = next
			continue
		}
		// either
		// 1. next is contained within curr
		// 2. next and curr overlap
		// 3. they're just kissing
		// either way, we only change the end of the range
		curr.end = max(curr.end, next.end)
	}

	total := 0

	for i := 0; i <= currIndex; i++ {
		interval := ranges[i]
		total += interval.end - interval.start + 1
	}

	return total
}

type idRange struct {
	start int
	end   int
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
