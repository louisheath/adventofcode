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
