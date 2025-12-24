Test input

```
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
```

represents tiles

```
..............
.......#...#..
..............
..#....#......
..............
..#......#....
..............
.........#.#..
..............
```

resulting in largest rectangle

```
..............
..OOOOOOOOOO..
..OOOOOOOOOO..
..OOOOOOOOOO..
..OOOOOOOOOO..
..OOOOOOOOOO..
..............
.........#.#..
..............
```

This is similar to the "container with most water" two-pointer leetcode, where the solution moves two pointers inwards, moving the pointer which is looking at the shorter wall.

I might be able to do this but require one wall to be tall and the other to be short, then do it again the other way around

Or I could just try every combination with brute force

## Part 2

Red tiles are joined together by green tiles. Together they form a loop. All tiles within the loop are green tiles. The created square must be within the area of red and green tiles.

I think I need to actually create the 2d array and draw out the joining green tiles. Filling the loop with green tiles doesn't feel straightforward. I could start from the edges and try to first fill the outside areas, but if the loop strands an island of non-green then I'll miss it. So I think I'll just average the red tile coordinates and hope that's within the green mass. Then colour-in from there.

I can then brute force my squares. If all four corners are within the coloured-in area then the square is eligible.
