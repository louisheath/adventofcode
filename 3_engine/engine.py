import sys

class Number:
  row: int
  left: int
  right: int
  value: int

  def __init__(self, row: int, left: int, right: int, value: int):
    self.row = row
    self.left = left
    self.right = right
    self.value = value

  def cols(self):
    return range(self.left, self.right + 1)

class Schema:
  rows: list
  height: int
  width: int

  # a map from coord adjecent to at least one symbol, to a list of
  # those symbols' coords
  valid_positions: {}
  all_numbers: list # []Number

  def __init__(self, file):
    self.rows = []
    self.height = 0
    self.width = 0
    self.all_numbers = []

    for line_bytes in file:
      line: str = line_bytes.decode("utf-8").strip("\n")
      self.rows.append(line)
      self.height += 1
      self.width = len(line)

    self.valid_positions = self.__valid_positions()
    self.__find_all_numbers()

  def __valid_positions(self) -> {}:
    valid = {}
    for row in range(self.height):
      for col in range(self.width):
        if self.__is_symbol(self.rows[row][col]):
          neighbours = [
            (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
            (row, col - 1), (row, col + 1),
            (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)
          ]
          for (r, c) in neighbours:
            symbols = valid.get((r, c), [])
            symbols.append((row, col))
            valid[(r, c)] = symbols
    return valid

  def __is_symbol(self, char: str) -> bool:
    return not char.isnumeric() and not char == "."

  def __find_all_numbers(self):
    for row in range(self.height):
      left = -1 # track the start and end of a number
      right = -1

      for col in range(self.width):
        element: str = self.rows[row][col]

        if element.isnumeric():
          if left == -1:
            left = col
          right = col

        else:
          if left != -1:
            num = int(self.rows[row][left:right + 1])
            self.all_numbers.append(Number(row, left, right, num))
          left = -1
          right = -1

      # check if row ended in number
      if left != -1:
        num = int(self.rows[row][left:right + 1])
        self.all_numbers.append(Number(row, left, right, num))

  def part_numbers(self):
    nums = []
    for num in self.all_numbers:
      for col in num.cols():
        valid = (num.row, col) in self.valid_positions
        if valid:
          nums.append(num.value)
          break
    return nums

  def gear_ratios(self):
    # map from asterisk coords to map of numbers coords to number
    asterisk_to_number = {} 

    for num in self.all_numbers:
      for col in num.cols():
        # the coords of all symbols around this digit
        symbol_coords = self.valid_positions.get((num.row, col))
        if symbol_coords is None:
          continue

        for (r, c) in symbol_coords:
          if self.rows[r][c] == "*":
            # an asterisk may be adjacent to multiple numbers
            numbers = asterisk_to_number.get((r, c), {})
            numbers[(num.row, num.left)] = num.value
            asterisk_to_number[(r, c)] = numbers

    gear_ratios = []

    for numbers in asterisk_to_number.values():
      if len(numbers) == 2:
        product = 1
        for number in numbers.values():
          product *= number
        gear_ratios.append(product)

    return gear_ratios

def main():
  with open(sys.argv[1], 'rb') as file:
    schema = Schema(file)

    part_numbers = schema.part_numbers()
    print("Part 1")
    print(sum(part_numbers)) # should be 517021

    ratios = schema.gear_ratios()
    print("Part 2")
    print(sum(ratios)) # should be 81296995

if __name__ == "__main__":
    # run with `python3 engine.py input2.txt`
    main()
