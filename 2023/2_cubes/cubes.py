import sys

upper_bounds = {
  "red": 12,
  "green": 13,
  "blue": 14,
}

def is_possible(max_seen: dict) -> bool:
    for colour in upper_bounds:
      if max_seen[colour] > upper_bounds[colour]:
        return False
    return True

def minimum_cubes(file) -> {}:
  id_to_min = {}

  for line_bytes in file:
    line: str = line_bytes.decode("utf-8").strip("\n")

    game_label, game = line.split(":")
    game_id = int(game_label.split(" ")[1])

    min_cubes = {
      "red": 0,
      "green": 0,
      "blue": 0,
    }

    for hand in game.split(";"):
      for set in hand.split(","):
        # `set` looks like " 10 red"
        _, num, colour = set.split(" ")
        min_cubes[colour] = max(min_cubes[colour], int(num))

    id_to_min[game_id] = min_cubes

  return id_to_min

def possible_ids(id_to_min: dict) -> []:
  ids = []
  for game_id in id_to_min:
    if is_possible(id_to_min[game_id]):
      ids.append(game_id)
  return ids

def game_powers(id_to_min: dict) -> []:
  powers = []
  for game_id in id_to_min:
    game = id_to_min[game_id]
    power = game["red"] * game["green"] * game["blue"]
    powers.append(power)
  return powers

def main():
  with open(sys.argv[1], 'rb') as file:
    id_to_min = minimum_cubes(file)

    possible = possible_ids(id_to_min)
    print("Part 1")
    print(sum(possible))

    powers = game_powers(id_to_min)
    print("Part 2")
    print(sum(powers))

if __name__ == "__main__":
    # run with `python3 cubes.py input2.txt`
    main()
