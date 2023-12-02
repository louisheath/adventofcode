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

def possible_game_ids(file) -> []:
  ids = []

  for line_bytes in file:
    line: str = line_bytes.decode("utf-8").strip("\n")

    game_label, game = line.split(":")
    game_id = int(game_label.split(" ")[1])

    max_seen = {
      "red": 0,
      "green": 0,
      "blue": 0,
    }

    for hand in game.split(";"):
      for set in hand.split(","):
        # `set` looks like " 10 red"
        _, num, colour = set.split(" ")
        max_seen[colour] = max(max_seen[colour], int(num))

    if is_possible(max_seen):
      ids.append(game_id)  

  return ids

def main():
  with open(sys.argv[1], 'rb') as file:
    ids = possible_game_ids(file)
    print(ids)
    print(sum(ids))

if __name__ == "__main__":
    # run with `python3 cubes.py input2.txt`
    main()
