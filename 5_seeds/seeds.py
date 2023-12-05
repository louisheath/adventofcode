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

  def get(self, src) -> int:
    for m in self.mapping:
      dest_lower, src_lower, src_upper = m
      if src >= src_lower and src < src_upper:
        return dest_lower + (src - src_lower)
    # if no mapping exists, return original
    return src
  
  # given a dest, find the src that maps to it, assuming
  # that the mapping is bijective
  def inverse(self, dest) -> int:
    for m in self.mapping:
      dest_lower, src_lower, src_upper = m
      length = src_upper - src_lower
      dest_upper = dest_lower + length
      if dest >= dest_lower and dest < dest_upper:
        return src_lower + (dest - dest_lower)
    return dest

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

  def locations_pt1(self):
    locations = []
    for seed in self.seeds:
      next = int(seed)
      for m in self.maps:
        next = m.get(next)
      locations.append(next)
    return locations

  def __seed_is_in_range(self, seed):
    for i in range(0, len(self.seeds), 2):
      start = int(self.seeds[i])
      length = int(self.seeds[i+1])
      if seed >= start and seed < start + length:
        return True
    return False

  def lowest_location_pt2(self) -> int:
    # now each number in `seeds` is not a seed, but each pair
    # represents a range of seeds.
    # there are too many seeds to try. work backwards, starting
    # at the lowest location, and searching for a matching seed.
    reversed_maps = list(reversed(self.maps))
    location = -1
    while True: 
      if location % 1000000 == 0:
        # it takes a while
        print(location)
      location += 1
      next = location
      for m in reversed_maps:
        next = m.inverse(next)
      # we know the seed that maps to the lowest location. is
      # it in the almanac's range of seeds?
      seed = next 
      if self.__seed_is_in_range(seed):
        return location

def main():
  with open(sys.argv[1], 'rb') as file:
    almanac = Almanac(file)

    pt1 = almanac.locations_pt1()
    print("Part 1")
    print(min(pt1)) # 525792406

    pt2 = almanac.lowest_location_pt2()
    print("Part 2")
    print(pt2) # 79004094

if __name__ == "__main__":
    # run with `python3 seeds.py input2.txt`
    main()
