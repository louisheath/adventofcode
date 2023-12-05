import time
import sys

class Mapping:
  # sorted list of (dest_lower, src_lower, src_upper)
  ranges: list

  def __init__(self):
    self.ranges = []

  def add_range(self, line):
    # e.g. line 50 98 2 means 98->50, 99->51
    dest, src_lower, length = line.split(" ")
    src_lower = int(src_lower)
    src_upper = src_lower + int(length)

    new_ranges = [
      (int(dest), src_lower, src_upper)  
    ]
    to_delete = []

    # trim any existing overlapping ranges
    for i in range(0, len(self.ranges)):
      (d, sl, su) = self.ranges[i]

      # range is above the new range. no overlap
      if sl >= src_upper:
        # all remaining ranges will also be above.
        break

      # range is below the new range. no overlap
      if su <= src_lower:
        continue

      # range ends mid-way through new.
      if sl < src_lower and su <= src_upper:
        self.ranges[i] = (d, sl, src_lower)
        continue

      # range starts mid-way through new.
      if sl >= src_lower and su > src_upper:
        incr = src_upper - sl
        self.ranges[i] = (d + incr, src_upper, su)
        continue
      
      # range sits within or is equal to new. remove it.
      if sl >= src_lower and su <= src_upper:
        to_delete.append(i)
        continue
     
      # range surrounds new. split it into two.
      if sl < src_lower and su > src_upper:
        self.ranges[i] = (d, sl, src_lower)
        incr = src_upper - sl
        new_ranges.append(
          (d + incr, src_upper, su)
        )
        continue

      print("this shouldn't be reachable")

    # delete ranges marked for deletion
    for i in reversed(to_delete):
      del self.ranges[i]

    # add range and sort
    self.ranges.extend(new_ranges)
    self.ranges.sort(key=lambda x: x[1])

  def get(self, src) -> int:
    for (dest_lower, src_lower, src_upper) in self.ranges:
      if src >= src_lower and src < src_upper:
        return dest_lower + (src - src_lower)
      if src_lower > src:
        # all remaining ranges will also be above.
        break
    # if no mapping exists, return original
    return src
  
  # given a dest, find the src that maps to it, assuming
  # that the mapping is bijective
  def inverse(self, dest) -> int:
    for r in self.ranges:
      dest_lower, src_lower, src_upper = r
      length = src_upper - src_lower
      dest_upper = dest_lower + length
      if dest >= dest_lower and dest < dest_upper:
        return src_lower + (dest - dest_lower)
    return dest

class Almanac:
  seeds: list # of string numbers
  seed_ranges: list # of tuples (start, length)
  mapping: Mapping

  def __init__(self, file):
    lines = [] # of str
    for line_bytes in file:
      line: str = line_bytes.decode("utf-8").strip("\n")
      lines.append(line)

    # line[0] ~= 'seeds: 79 14 55 13'
    self.seeds = lines[0].split(" ")[1:]
    self.maps = []

    # convert seeds to tuples and sort in ascending order
    self.seed_tuples = []
    for i in range (0, len(self.seeds), 2):
      start, length = int(self.seeds[i]), int(self.seeds[i+1])
      self.seed_tuples.append((start, length))
    self.seed_tuples.sort(key=lambda x: x[0])

    # build one big mapping function
    self.mapping = Mapping()
    for i in range(3, len(lines)):
      line = lines[i]
      if line == "": # end of map
        continue
      if " map:" in line:
        continue
      self.mapping.add_range(line)

  def locations_pt1(self):
    locations = []
    for seed in self.seeds:
      locations.append(
        int(self.mapping.get(int(seed)))
      )
    return locations

  # def __seed_is_in_range(self, seed):
  #   for (start, length) in self.seed_tuples:
  #     if seed < start:
  #       # the seed is smaller than this range and all later ranges,
  #       # as we ordered the list
  #       return False
  #     if seed >= start and seed < start + length:
  #       return True
  #   return False

  # def lowest_location_pt2(self) -> int:
  #   # now each number in `seeds` is not a seed, but each pair
  #   # represents a range of seeds.
  #   # there are too many seeds to try. work backwards, starting
  #   # at the lowest location, and searching for a matching seed.
  #   reversed_maps = list(reversed(self.maps))
  #   location = -1
  #   while True: 
  #     if location % 1000000 == 0:
  #       # it takes a while
  #       print(location)
  #     location += 1
  #     next = location
  #     for m in reversed_maps:
  #       next = m.inverse(next)
  #     # we know the seed that maps to the lowest location. is
  #     # it in the almanac's range of seeds?
  #     seed = next 
  #     if self.__seed_is_in_range(seed):
  #       return location

def main():
  with open(sys.argv[1], 'rb') as file:
    almanac = Almanac(file)

    pt1 = almanac.locations_pt1()
    print("Part 1")
    print(min(pt1)) # 525792406

    # pt2 = almanac.lowest_location_pt2()
    # print("Part 2")
    # print(pt2) # 79004094

if __name__ == "__main__":
    # run with `python3 seeds.py input2.txt`
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    # a611789 - 733.5s
    # 74a16da - 603.6s
