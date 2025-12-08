file = open('input.txt', 'r')
CONNS = 1000
boxes = [(int(l[0]), int(l[1]), int(l[2])) for l in [l.strip().split(",") for l in file.readlines()]]

def dist(a, b):
  return (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2

junctions = {}
dists = []
sets = []
for i in range(len(boxes)):
  for j in range(i+1, len(boxes)):
    d = dist(boxes[i], boxes[j])
    dists.append((d, i, j))
dists.sort()

for t in range(CONNS):
  d, i, j = dists[t]
  if (i not in junctions) and (j not in junctions):
    s = {i, j}
    sets.append(s)
    junctions[i] = junctions[j] = len(sets)-1
  elif i not in junctions:
    sets[junctions[j]].add(i)
    junctions[i] = junctions[j]
  elif j not in junctions:
    sets[junctions[i]].add(j)
    junctions[j] = junctions[i]
  elif junctions[i] == junctions[j]: # already connected
    t -= 1
  else:
    for x in sets[junctions[i]]:
      sets[junctions[j]].add(x)
      junctions[x] = junctions[j]

# find largest 3 junctions
jSizes = [len(sets[l]) for l in set(junctions.values())]
jSizes.sort(reverse=True)
product = 1
for p in jSizes[:3]:
  product *= p
print(product)

  
