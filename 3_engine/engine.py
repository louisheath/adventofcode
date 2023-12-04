import sys

class Schema:
  rows: list
  height: int
  width: int
  valid_positions: {}
  part_numbers: list

  def __init__(self, file):
    self.rows = []
    self.height = 0
    self.width = 0
    self.part_numbers = []

    for line_bytes in file:
      line: str = line_bytes.decode("utf-8").strip("\n")
      self.rows.append(line)
      self.height += 1
      self.width = len(line)

    self.valid_positions = self.__valid_positions()
    self.__calculate_part_numbers()

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
            valid[(r, c)] = True
    return valid

  def __is_symbol(self, char: str) -> bool:
    return not char.isnumeric() and not char == "."

  def __calculate_part_numbers(self):
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
            self.__add_part_number(row, left, right)
          left = -1
          right = -1

      # check if row ended in number
      if left != -1:
        self.__add_part_number(row, left, right)
          
  def __add_part_number(self, row: int, left: int, right: int):
    number = int(self.rows[row][left:right + 1])
    for col in range(left, right + 1):
      valid = (row, col) in self.valid_positions
      if valid:
        self.part_numbers.append(number)
        return

def main():
  with open(sys.argv[1], 'rb') as file:
    schema = Schema(file)
    print(sum(schema.part_numbers))
    return

if __name__ == "__main__":
    # run with `python3 engine.py input2.txt`
    main()
