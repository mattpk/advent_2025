file = open('input.txt', 'r')
lines = [l.strip() for l in file.readlines()]
sum = 0

def backtrack(state, desired, buttons, i):
  if i >= len(buttons): return 0 if state == desired else 100000
  ans = backtrack(state, desired, buttons, i + 1)
  for b in buttons[i]:
    state[b] = not state[b]
  ans = min(ans, 1 + backtrack(state, desired, buttons, i + 1))
  for b in buttons[i]:
    state[b] = not state[b]
  return ans

for line in lines:
  sq_start = line.index("[")
  sq_end = line.index("]")
  joltage_start = line.index("{")
  buttons = [[int(x) for x in b] for b in [l.strip()[1:-1].split(',') for l in line[sq_end+1:joltage_start].split()]]

  desired_state = [0 if c == '.' else 1 for c in line[sq_start+1:sq_end]]
  state = [0 for _ in desired_state]
  presses = backtrack(state, desired_state, buttons, 0)
  sum += presses

print(sum)