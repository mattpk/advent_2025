file = open('input.txt', 'r')
lines = [l.strip() for l in file.readlines()]
count = 0

width = len(lines[0])

tachyons = set()
tachyons.add(lines[0].find('S'))
for i in range(1,len(lines)):
  line = lines[i]
  newts = set()
  for t in tachyons:
    newts.add(t)
  for j in tachyons:
    if line[j] == '^':
      newts.remove(j)
      if j > 0:
        newts.add(j-1)
      if j < len(line) - 1:
        newts.add(j+1)
      count += 1
  tachyons = newts
print(count)
