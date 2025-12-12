import sys

class ScratchCard:
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

class ScratchCardTable:
  cards: list # []ScratchCard

  def __init__(self, file):
    self.cards = []
    for line_bytes in file:
      line: str = line_bytes.decode("utf-8").strip("\n")
      self.cards.append(ScratchCard(line))

  def scores(self) -> int:
    scores = []
    for card in self.cards:
      scores.append(card.score())
    return scores
  
  def total_cards(self) -> int:
    # to start, we have one of each card
    counts = []
    for i in range(0, len(self.cards)):
      counts.append(1)

    for i in range(0, len(self.cards)):
      card = self.cards[i]
      # if card 1 scores 1, we get an extra card 2
      # if card 2 scores 2, we get extras of 3 and 4.
      # if we had two card 2s, we'd get 2x of 3 and 4
      wins = card.wins()

      # add the cards we won
      for j in range(1, wins + 1):
        counts[i + j] += counts[i]
    
    return sum(counts)

def main():
  with open(sys.argv[1], 'rb') as file:
    table = ScratchCardTable(file)

    scores = table.scores()
    print("Part 1")
    print(sum(scores)) # 20117

    print("Part 2")
    print(table.total_cards()) # 13768818

if __name__ == "__main__":
    # run with `python3 scratchcard.py input3.txt`
    main()
