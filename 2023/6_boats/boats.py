import sys

def winning_strategies(race: list) -> list:
  strats = [] # of ints
  (time, record_distance) = race
  for speed in range(1, time):
    time_to_race = time - speed
    distance = speed * time_to_race
    if distance > record_distance:
      strats.append(speed)
  return strats

def part1(lines: list) -> int:
  races = [] # of tuple (time, distance)
  for t in lines[0][9:].split(" "):
      if t == "": continue
      races.append([int(t), 0])
  i = 0
  for d in lines[1][9:].split(" "):
    if d == "": continue
    races[i][1] = int(d)
    i += 1

  product = 1
  for race in races:
    strats = winning_strategies(race)
    product *= len(strats)
  return product 

def part2(lines: list) -> int:
  time = ""
  for t in lines[0][9:].split(" "):
      if t == "": continue
      time += t # concat
  dist = ""
  for d in lines[1][9:].split(" "):
    if d == "": continue
    dist += d

  race = [int(time), int(dist)]
  return len(winning_strategies(race)) 

def main():
  with open(sys.argv[1], 'rb') as file:
    lines = [] # of str
    for line_bytes in file:
      line: str = line_bytes.decode("utf-8").strip("\n")
      lines.append(line)

    print("Part 1")
    print(part1(lines)) # 2269432

    print("Part 2")
    print(part2(lines)) # 35865985

if __name__ == "__main__":
    # run with `python3 boats.py input2.txt`
    main()
