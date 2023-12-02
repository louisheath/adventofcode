import sys

class FirstAndLastDigits:
  first = -1
  last = -1

  def track_new_digit(self, digit):
    if self.first == -1:
      self.first = digit
    self.last = digit

  def final_number(self):
    return int(str(self.first) + str(self.last))

def is_digit(char):
  return char >= 48 and char <= 57

def matches_word(i, line):
  return -1

def ascii_to_int(char):
  return char - 48

def calibration_values(file):
  vals = []

  for line in file:
    tracker = FirstAndLastDigits()

    for i in range(0, len(line)):
      char = line[i]

      if is_digit(char):
        digit = ascii_to_int(char)
        tracker.track_new_digit(digit)
        continue

      matched_digit = matches_word(i, line)
      if matched_digit != -1:
        tracker.track_new_digit(matched_digit)
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
