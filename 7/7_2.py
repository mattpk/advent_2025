file = open('input.txt', 'r')
lines = [l.strip() for l in file.readlines()]
count = 0

width = len(lines[0])
saved = {}

def dfs(lines, tachyon, height):
  if (tachyon, height) in saved:
    return saved[(tachyon, height)]
  if height >= len(lines): return 1
  ans = 0
  if lines[height][tachyon] == '^':
    ans = dfs(lines, tachyon-1, height+1) + dfs(lines, tachyon+1, height+1)
  else:
    ans = dfs(lines, tachyon, height+1)
  saved[(tachyon, height)] = ans
  return ans

count = dfs(lines, lines[0].find('S'), 0)

print(count)
