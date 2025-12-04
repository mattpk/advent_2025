file = open('input.txt', 'r')
lines = [l.strip() for l in file.readlines()]
empty = ['.'] * (len(lines[0]) + 2)
grid = [empty] + [list(c for c in '.' + line + '.') for line in lines] + [empty]
count = 0
for i in range(1, len(grid) - 1):
  for j in range(1, len(grid[0]) - 1):
    if grid[i][j] != '@':
      continue
    adj = 0
    adj += 1 if grid[i-1][j] == '@' else 0
    adj += 1 if grid[i+1][j] == '@' else 0
    adj += 1 if grid[i][j-1] == '@' else 0
    adj += 1 if grid[i][j+1] == '@' else 0
    adj += 1 if grid[i+1][j+1] == '@' else 0
    adj += 1 if grid[i-1][j+1] == '@' else 0
    adj += 1 if grid[i+1][j-1] == '@' else 0
    adj += 1 if grid[i-1][j-1] == '@' else 0
    if adj < 4:
      count += 1
print(count)

