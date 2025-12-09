import sys
sys.setrecursionlimit(1000000) # for floodfill

file = open('input.txt', 'r')
lines = [(int(i), int(j)) for j, i in [l.strip().split(",") for l in file.readlines()]]

# There was a stacked window tint problem back in CCC
# Reyno blew my mind by telling me he solved it with coordinate compression
# This does a similar thing, it's fast enough for the inputs

# add extra border so we can floodfill at 0,0
rs = {-10000000, 10000000}
cs = {-10000000, 10000000}
for i, j in lines:
  rs.add(i)
  cs.add(j)

rows = sorted(list(rs))
cols = sorted(list(cs))

rowMap = {}
colMap = {}
for i in range(len(rows)):
  rowMap[rows[i]] = i
for i in range(len(cols)):
  colMap[cols[i]] = i

coords = [(rowMap[i], colMap[j]) for i, j in lines]
grid = [[0 for _ in range(len(cols))] for _ in range(len(rows))]

(pi, pj) = coords[-1]
for i, j in coords:
  if (pj == j):
    for x in range(pi, i, 1 if pi < i else -1):
      grid[x][j] = 1
  else:
    for x in range(pj, j, 1 if pj < j else -1):
      grid[i][x] = 1
  pi, pj = i, j

def fill(i, j):
  if i < 0 or j < 0 or i >= len(cols) or j >= len(rows) or grid[i][j] != 0:
    return
  grid[i][j] = 2
  fill(i+1, j)
  fill(i-1, j)
  fill(i, j+1)
  fill(i, j-1)

fill(0,0)

def check(pi, pj, i, j):
  if (i < pi): return check(i, j, pi, pj)
  step = 1 if j >= pj else -1
  for row in range(pi, i+1):
    for col in range(pj, j + step, step):
      if grid[row][col] == 2:
        return False
  return True

best = 0
for pi, pj in lines:
  for i, j in lines:
    if (check(rowMap[pi], colMap[pj], rowMap[i], colMap[j])):
      best = max(best, ((abs(pi-i)+1) * (abs(pj-j)+1)))

print(best)
  