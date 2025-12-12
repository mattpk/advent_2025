file = open('input.txt', 'r')
lines = [l.strip() for l in file.readlines()]

shapes = []
index = -1
for i, line in enumerate(lines):
  if 'x' in line: 
    index = i
    break
  elif ':' in line:
    index = int(line[0])
    shapes.append([])
  elif line != '':
    shapes[index].append(line)

weights = [sum([sum([1 if c =='#' else 0 for c in row]) for row in s]) for s in shapes]

sum = 0
for line in lines[index:]:
  colon_index = line.find(':')
  x_index = line.find('x')
  w = int(line[:x_index])
  l = int(line[x_index+1:colon_index])

  # check if its even possible to fit all the pieces
  weight = 0
  for i, c in enumerate([int(x) for x in line[colon_index+1:].split()]):
    weight += c * weights[i]
  print(w * l - weight) # Wow, this revealed the tricky input
  if (w * l < weight): continue
  sum += 1

print(sum)

  

