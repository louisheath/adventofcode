package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	fmt.Println(laboratories())
}

func readFile(filePath string) []string {
	file, err := os.Open(filePath)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	lines := []string{}
	for scanner.Scan() {
		// Text converts to string and drops newline character
		lines = append(lines, scanner.Text())
	}

	// Check for errors during scanning
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return lines
}
