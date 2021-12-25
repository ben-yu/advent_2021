import sys
from collections import defaultdict

with open('day_24_input.txt', 'r') as f:
  l = [line.split() for line in f.readlines()]

  const = []
  for i in range(14):
      off = i * 18
      A = int(l[4+off][2])
      B = int(l[5+off][2])
      C = int(l[15+off][2])
      const.append((A,B,C))
  for i,c in enumerate(const):
      print(i,c)

# Equations derived from input
# ================
# d3 + 13 = d4 + 6
# d5 + 13 = d6 +12
# d9 + 10 = d10 + 2
# d8 + 11 = d11 + 5
# d7 + 3 = d12 + 4
# d2 + 2 = d13 + 4
# d1 + 6 = d14 + 12