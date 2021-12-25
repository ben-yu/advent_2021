import copy

width = 139
height = 137

def pretty_print(grid):
  for i in range(height):
    row = ''
    for j in range(width):
      row += grid[(i,j)]
    print(row)

def iterate(grid):
  updated = False
  copy_grid = copy.deepcopy(grid)
  for pos, v in grid.items():
    if v == ">":
      y = (pos[1] + 1) % width
      if grid[(pos[0], y)] == '.':
        updated = True
        copy_grid[(pos[0], y)] = '>'
        copy_grid[(pos[0], pos[1])] = '.'

  grid = copy.deepcopy(copy_grid)

  for pos, v in grid.items():
    #print(pos,v)
    if v == "v":
      x = (pos[0] + 1) % height
      if grid[(x, pos[1])] == '.':
        updated = True
        copy_grid[(x, pos[1])] = 'v'
        copy_grid[(pos[0], pos[1])] = '.'

  return updated, copy_grid

with open('day_25_input.txt','r') as f:
  lines = f.readlines()

  grid = {}
  for i, l in enumerate(lines):
    for j, c in enumerate(list(l.strip())):
      grid[(i,j)] = c

  pretty_print(grid)
  updated, grid = iterate(grid)
  pretty_print(grid)

  steps = 1
  while updated:
    updated, grid = iterate(grid)
    steps += 1

    print("After {} steps:".format(steps))
    pretty_print(grid)

