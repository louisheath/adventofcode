import sys
from functools import cmp_to_key

cards = {
  "J": 1,
  "2": 2,
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9,
  "T": 10,
  "Q": 12,
  "K": 13,
  "A": 14,
}

five_of_a_kind = 6
four_of_a_kind = 5
full_house = 4
three_of_a_kind = 3
two_pair = 2
one_pair = 1
high_card = 0

def add_jokers(rank: str, jokers: int) -> int:
  if jokers == 0 or rank == five_of_a_kind:
    return rank

  # depending on the current hand, determine
  # what new hand is possible with jokers.
  new_rank = {}

  if rank == high_card:
    new_rank = {
      1: one_pair, 
      2: three_of_a_kind, 
      3: four_of_a_kind, 
      4: five_of_a_kind 
    }
  elif rank == one_pair:
    new_rank = {
      1: three_of_a_kind,
      2: three_of_a_kind,
    }
  elif rank == two_pair:
    new_rank = {
      1: full_house,
      2: four_of_a_kind,
    }
  elif rank == three_of_a_kind:
    new_rank = {
      1: four_of_a_kind,
      2: five_of_a_kind
    }
  elif rank == full_house:
    new_rank = {
      2: five_of_a_kind,
      3: five_of_a_kind
    }
  elif rank == four_of_a_kind:
    new_rank = {
      1: five_of_a_kind,
      4: five_of_a_kind,
    }

  return new_rank[jokers]

class Hand:
  cards: str
  bid: int
  type: str
  jokers: int

  def __init__(self, line: str):
    cards, bid = line.split(" ")
    self.cards = cards
    self.bid = int(bid)

    grouped = {}
    for card in cards:
      count = grouped.get(card, 0)
      count += 1
      grouped[card] = count
    counts = grouped.values()

    type = high_card
    if len(grouped) == 1:
      type = five_of_a_kind
    elif len(grouped) == 2:
      if 4 in counts:
        type = four_of_a_kind
      else:
        type = full_house
    elif len(grouped) == 3:
      if 3 in counts:
        type = three_of_a_kind
      else:
        type = two_pair
    elif len(grouped) == 4:
      type = one_pair

    jokers = grouped.get("J", 0)

    self.type = add_jokers(type, jokers)

def compare(h1: Hand, h2: Hand):
  if h1.type == h2.type:
    for i in range(0, 5):
      card1, card2 = h1.cards[i], h2.cards[i]
      if card1 == card2:
        continue
      if cards[card1] < cards[card2]:
        return -1
      else:
        return 1
    # a draw
    return -1
  elif h1.type < h2.type:
      return -1
  else:
    return 1

def part1(lines: list) -> int:
  hands = []
  for line in lines:
    hands.append(Hand(line))

  sorted_hands = sorted(hands, key=cmp_to_key(compare))

  winnings = 0
  for i in range(0, len(sorted_hands)):
    rank = i + 1
    winnings += rank * sorted_hands[i].bid

  return winnings

def main():
  with open(sys.argv[1], 'rb') as file:
    lines = [] # of str
    for line_bytes in file:
      line: str = line_bytes.decode("utf-8").strip("\n")
      lines.append(line)

    # Part 1 248217452 (J -> 11, rmv `add_jokers`)

    print("Part 2")
    print(part1(lines)) # 245576185

if __name__ == "__main__":
  # run with `python3 cards.py input2.txt`
  main()
