package main

import (
	"log"
	"strconv"
	"strings"
)

func giftShop() int {
	file := readFile("2_input.txt")
	ranges := strings.Split(file[0], ",")

	answer := 0

	for _, r := range ranges {
		s := strings.Split(r, "-")
		start, err := strconv.Atoi(s[0])
		if err != nil {
			log.Fatal(err)
		}
		end, err := strconv.Atoi(s[1])
		if err != nil {
			log.Fatal(err)
		}

		for i := start; i <= end; i++ {
			str := strconv.Itoa(i)
			if len(str) < 2 {
				continue
			}
			// Try all prefixes as potential repeated patterns
			for j := 1; j < len(str)/2+1; j++ {
				if len(str)%j != 0 {
					continue
				}
				pattern := str[:j]
				if str == strings.Repeat(pattern, len(str)/j) {
					answer += i
					break
				}
			}
		}
	}

	return answer
}
