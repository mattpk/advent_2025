file = open('input.txt', 'r')
lines = [(int(i), int(j)) for i, j in [l.strip().split(",") for l in file.readlines()]]


map = {}
for row, col in lines:
  if not col in map:
    map[col] = (row, row)
  else:
    pmin, pmax = map[col]
    map[col] = (min(pmin, row), max(pmax, row))
keys = list(map)
best = 0

for i in keys:
  top = map[i][0]
  for j in keys:
    best = max(best, (abs(i-j) + 1) * (map[j][1] - top + 1))

print(best)