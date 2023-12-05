import sys

class Map:
  mapping: list # of tuples (dest, src_lower, src_upper)

  def __init__(self):
    self.mapping = []

  def add_mapping(self, line):
    # e.g. line 50 98 2 means 98->50, 99->51
    dest, src, length = line.split(" ")
    self.mapping.append(
      (int(dest), int(src), int(src)+int(length))
    )

  def is_empty(self) -> bool:
    return len(self.mapping) == 0

  def get(self, src)-> int:
    for m in self.mapping:
      dest_lower, src_lower, src_upper = m
      if src >= src_lower and src < src_upper:
        return dest_lower + (src - src_lower)
    # if no mapping exists, return original
    return src
  
class Almanac:
  seeds: list # of string numbers
  maps: list # of Maps

  def __init__(self, file):
    lines = [] # of str
    for line_bytes in file:
      line: str = line_bytes.decode("utf-8").strip("\n")
      lines.append(line)

    # line[0] ~= 'seeds: 79 14 55 13'
    self.seeds = lines[0].split(" ")[1:]
    self.maps = []

    # split and parse each map
    current_map = Map()
    for i in range(3, len(lines)):
      line = lines[i]
      if line == "": # end of map
        self.maps.append(current_map)
        current_map = Map()
        continue
      if " map:" in line:
        continue
      current_map.add_mapping(line)

    if not current_map.is_empty():
      self.maps.append(current_map)

  def locations(self):
    locations = []
    for seed in self.seeds:
      next = int(seed)
      for m in self.maps:
        next = m.get(next)
      locations.append(next)
    return locations

def main():
  with open(sys.argv[1], 'rb') as file:
    almanac = Almanac(file)

    locations = almanac.locations()
    print("Part 1")
    print(min(locations)) # 525792406

if __name__ == "__main__":
    # run with `python3 seeds.py input2.txt`
    main()
