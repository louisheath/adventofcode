import sys

class ScratchCardRow:
  winning: set
  scratched: list

  def __init__(self, line: str):
    self.winning = set()
    self.scratched = list()

    [_, numbers] = line.split(": ")
    [winning, scratched] = numbers.split(" | ")

    for winning_number in winning.split(" "):
      if winning_number == "":
        continue
      self.winning.add(int(winning_number))

    for scratched_number in scratched.split(" "):
      if scratched_number == "":
        continue
      self.scratched.append(int(scratched_number))
  
  def wins(self) -> int:
    wins = 0
    for scratched_number in self.scratched:
      if scratched_number in self.winning:
        wins += 1
    return wins
  
  def score(self) -> int:
    wins = self.wins()
    if wins == 0:
      return 0
    score = 1
    for _ in range(wins - 1):
      score *= 2
    return score

class ScratchCard:
  rows: list # []ScratchCardRow

  def __init__(self, file):
    self.rows = []
    for line_bytes in file:
      line: str = line_bytes.decode("utf-8").strip("\n")
      self.rows.append(ScratchCardRow(line))

  def scores(self) -> int:
    scores = []
    for row in self.rows:
      scores.append(row.score())
    return scores

def main():
  with open(sys.argv[1], 'rb') as file:
    card = ScratchCard(file)

    scores = card.scores()
    print("Part 1")
    print(sum(scores))

if __name__ == "__main__":
    # run with `python3 scratchcard.py input2.txt`
    main()
