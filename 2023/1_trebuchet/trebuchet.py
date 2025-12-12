import sys

numbers = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9,
}

class FirstAndLastDigits:
  first = -1
  last = -1

  def track_new_digit(self, digit: int) -> None:
    if self.first == -1:
      self.first = digit
    self.last = digit

  def final_number(self) -> int:
    return int(str(self.first) + str(self.last))

def is_digit(char: int) -> bool:
  return char >= 48 and char <= 57

def ascii_to_int(char: int) -> int:
  return char - 48

def matches_word(i: int, line: str) -> [bool, int]:
  for word in numbers:
    if line[i:i+len(word)] == word:
      return [True, numbers[word]]
  return [False, -1]

def calibration_values(file) -> []:
  vals = []

  for line_bytes in file:
    line: str = line_bytes.decode("utf-8")
    tracker = FirstAndLastDigits()

    for i in range(0, len(line)):
      char: int = line_bytes[i]

      if is_digit(char):
        digit = ascii_to_int(char)
        tracker.track_new_digit(digit)
        continue

      [matches, digit] = matches_word(i, line)
      if matches:
        tracker.track_new_digit(digit)
        continue

    vals.append(tracker.final_number())

  return vals

def main():
  with open(sys.argv[1], 'rb') as file:
    vals = calibration_values(file)
    print(vals)
    print(sum(vals))

if __name__ == "__main__":
    # run with `python3 trebuchet.py input2.txt`
    main()
