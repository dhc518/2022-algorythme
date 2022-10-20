
#from data_city import City, five_letter_cities
from random import randint, seed, shuffle
from math import sqrt

class City:
  def __init__(self, name, x, y, index=0):
    self.name = name
    self.x, self.y = x, y
    self.index = index
  def __repr__(self):
    return f'{self.name}({self.index}:{self.x:3d},{self.y:3d})'

cities = [
  City("Bases", 742, 531, 63),
  City("Atone", 1037, 630, 64),
  City("Knife", 1025, 879, 65),
  City("Seise", 377, 257, 66),
  City("Odour", 614, 553, 67),
  City("Venom", 481, 676, 68),
  City("Filmy", 943, 53, 69),
  City("Barre", 88, 9, 70),
  City("Davit", 28, 271, 71),
  City("Smart", 952, 279, 72),
  City("Canon", 1426, 519, 73),
  City("Dixie", 699, 698, 74),
  City("Pease", 925, 716, 75),
  City("Adorn", 1132, 414, 76),
  City("Liver", 1371, 238, 77),
  City("Druid", 1389, 689, 78),
  City("Baked", 1573, 774, 79),
  City("Tulip", 915, 636, 80),
  City("Unzip", 941, 763, 81),
  City("Nervy", 1083, 385, 82),
  City("Hubby", 1297, 588, 83),
]

#from math imprort sqrt
import math

def distance(c1, c2):
  return math.sqrt((c1.x - c2.x) ** 2 + (c1.y - c2.y) ** 2)


def closest_of_three(array, start, end): #end=inclusive
  size = end - start + 1
  if size != 3:
    print(f'Size is mot 3; {size}')
    exit(0)

  # return start, end, 10.123

  d1 = distance( array[start], array[start+1])
  d2 = distance( array[start], array[start+2])
  d3 = distance( array[start+1], array[start+2])

  if d1 < d2 and d1 <= d3:
    return start, start+1, d1
  elif d2 <= d3:
    return start, start+1, d2

  return start, start+1, d3


def closest_pair(array, start, end): #end=inclusive
  size = end - start + 1
  if size <= 1:
    print(f'BUG!!! Size is <= 1; {size}')
    exit(0)
  if size == 2:
    return start, end, distance(array[start], array[end])
  if size == 3:
    return closest_pair(array, start, end)

   # mid = start + size // 2 -1
  last_left = (start + end) // 2 #3개 2개 나누기
  ls, le, ld = closest_pair(array, start, last_left)
  rs, re, rd = closest_pair(array, last_left+1, end)

  s, e, d = ls, le, ld if ld <= rd else (rs, re, rd)

  x1 = array[last_left].x - d
  x2 = array[last_left].x + d

  # 1st
  '''
  strip = []
  for i in range(start, end+1):
    c = cities[i]
    if x1 <= c.x and c.x <= x2:
      strip.append(c)
  '''
  #2nd
  #strip = [ c for c in cities[start:end+1] if x1 <= c.x and c.x <= x2]

  #3rd
  '''
  strip = [ c for c in cities\
   if x1 <= c.x and c.x <= x2 and \
            start <= c.index and c.indes <= end
            
  ]
  '''
  i1 = min(c.index for c in cities if c.x >= x1 and c.index >= start)
  i2 = max(c.index for c in cities if c.x <= x2 and c.index <= end)

  #strip = cities[i1:i2:i2+1]

  #strip.sort(key=lambda c: c.y)

  strip = [c for c in cities_y if i1 <= c.index and c.index <= i2]

  n_strip = len(strip)
  for i1 in range(n_strip):
    c1 = strip[i1]
    for i2 in range(i1+1, n_strip):
      c2 = strip[i2]
      dy = c2.y - c1.y
      if dy > d:
        break

      dd = math.sqtr((c1.x - c2.x) ** 2 + dy ** 2)
      if dd < d:
        s, e, d = c1.index, c2.index, dd

  return s, e, d

n_cities = len(cities)
print('정렬 전', cities)
cities.sort(key=lambda c: c.x)
for i in range(n_cities):
  cities[i].index = i
print('정렬 후',cities)


cities_y = sorted(cities, key=lambda c:c.y)

#closest_of_three(cities, 0, n_cities - 1)
s, e, d = closest_pair(cities, 0, n_cities - 1)
print(f'{cities[s]} ~ {cities[e]} : {d:.1f}')

#Pease = Unzip 49.6




