file = open('input.txt', 'r')
lines = [l.strip() for l in file.readlines()]

graph = {'out': []}
for line in lines:
  colon_index = line.index(":")
  f = line[:colon_index].strip()
  graph[f] = []
  for target in line[colon_index+1:].split():
      graph[f].append(target)

def num_ways(start, goal):
    mem = {}
    for key in graph:
      mem[key] = {}
    mem[goal] = {0: 1}
    length = 1
    changed = True
    while changed:
      changed = False
      for key in mem:
        for n in graph[key]:
          if (length-1) in mem[n]:
            if length not in mem[key]: mem[key][length] = 0
            mem[key][length] += mem[n][length-1]
            changed = True
      length+=1
    return sum(mem[start].values())

print(num_ways('svr', 'dac') * num_ways('dac', 'fft') * num_ways('fft', 'out') + num_ways('svr', 'fft') * num_ways('fft', 'dac') * num_ways('dac', 'out'))