import sys

class Schema:
  rows: list
  height: int
  width: int
  valid_positions: {}

  def __init__(self, file):
    self.rows = []
    self.height = 0
    self.width = 0

    for line_bytes in file:
      line: str = line_bytes.decode("utf-8").strip("\n")
      self.rows.append(line)
      self.height += 1
      self.width = len(line)

    self.valid_positions = self.__valid_positions()

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
            if not self.__out_of_bounds(r, c):
              valid[(r, c)] = True
    return valid

  def __is_symbol(self, char: str) -> bool:
    return not char.isnumeric() and not char == "."
  
  def __out_of_bounds(self, row: int, col: int) -> bool:
    return (row < 0 or col < 0 or
      row >= self.height or col >= self.width)

  def part_numbers(self) -> list:
    part_numbers = []

    for row in range(self.height):
      # left and right track the start and end of a number
      left = -1
      right = -1

      for col in range(self.width):
        element: str = self.rows[row][col]

        if element.isnumeric():
          if left == -1:
            left = col
          right = col

        else:
          if left != -1:
            part_numbers = self.__add_part_number(
              row, left, right, part_numbers,
            )
          left = -1
          right = -1

      # check if row ended in number
      if left != -1:
        part_numbers = self.__add_part_number(
          row, left, right, part_numbers,
        )

    return part_numbers
          
  def __add_part_number(
      self, row: int, left: int, right: int, part_numbers: list,
  ) -> list:
    number = int(self.rows[row][left:right + 1])
    for col in range(left, right + 1):
      valid = (row, col) in self.valid_positions
      if valid:
        part_numbers.append(number)
        return part_numbers
    return part_numbers

def main():
  with open(sys.argv[1], 'rb') as file:
    schema = Schema(file)
    part_numbers = schema.part_numbers()
    print(sum(part_numbers))
    return

if __name__ == "__main__":
    # run with `python3 engine.py input2.txt`
    main()
