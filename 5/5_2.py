import math
file = open('input.txt', 'r')
lines = [l.strip() for l in file.readlines()]
ranges = [(int(i), int(j)+1) for i, j in [l.split('-') for l in lines[:lines.index("")]]]
ranges.sort(key=lambda i: i[0]) 
count = 0
last = -1

for i, j in ranges:
  if j < last:
    continue
  count += j - max(i, last)
  last = max(last, j)
print(count)
