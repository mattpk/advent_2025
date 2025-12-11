file = open('input.txt', 'r')
lines = [l.strip() for l in file.readlines()]

graph = {}
for line in lines:
  colon_index = line.index(":")
  f = line[:colon_index].strip()
  graph[f] = []
  for target in line[colon_index+1:].split():
      graph[f].append(target)

def num_paths(graph, pos, seen):
   if pos == 'out': return 1
   if pos in seen: return 0
   seen.add(pos)
   ans = 0
   for n in graph[pos]:
      ans += num_paths(graph, n, seen)
   seen.remove(pos)
   return ans

seen = set()
print(num_paths(graph, 'you', seen))