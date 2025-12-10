# Below is a mess of backtracking with pruning before I realized it wasn't fast enough.
# The intended solution seems to be to import a linear optimizer and plug in the problem's system of equations.

file = open('input.txt', 'r')
lines = [l.strip() for l in file.readlines()]
sum = 0

def backtrack(state, can_press, index, button_index):
  if index == len(state): return 0
  if state[index] == 0: return backtrack(state, can_press, index + 1, 0)
  if button_index >= len(can_press[index]): return 10000
  orig = list(state)
  length = state[index]
  ans = backtrack(state, can_press, index, button_index+1)
  if (ans < 10000): return ans
  i = length
  while i > 0:
    skip = 0
    for b in can_press[index][button_index]:
      state[b] = orig[b] - i
      if (state[b] < skip):
        skip = state[b]
    if skip == 0:
      ans = i + backtrack(state, can_press, index, button_index+1)
      if (ans < 10000): return ans
    else:
      i += skip + 1
    for l in range(len(state)): state[l] = orig[l]
    i -= 1
  return ans

for line in lines:
  sq_end = line.index("]")
  joltage_start = line.index("{")
  joltage_end = line.index("}")
  buttons = [[int(x) for x in b] for b in [l.strip()[1:-1].split(',') for l in line[sq_end+1:joltage_start].split()]]
  desired_state = [int(x) for x in line[joltage_start+1:joltage_end].split(',')]

  # for each index, make a list of the buttons it can press -- buttons can not appear in later indices
  can_press = [[] for _ in desired_state]
  for i, lst in enumerate(can_press):
    new_buttons = list(buttons)
    for b in buttons:
      if i in b:
        new_buttons.remove(b)
        lst.append(b)
    lst.sort(key = lambda x: -len(x))
    buttons = new_buttons
  presses = backtrack(desired_state, can_press, 0, 0)
  sum += presses

print(sum)