file = open('input.txt', 'r')
lines = [l for l in file.readlines()]

height = len(lines)
width = len(lines[0])
count = 0

sum = 0
for i in range(width):
  if lines[height-1][i] in ['*', '+']:
    count += sum
    op = lines[height-1][i]
    sum = 1 if op == "*" else 0
  
  num = 0
  for j in range(height-1):
    if not lines[j][i].isdigit(): continue
    num *= 10
    num += int(lines[j][i])
  if num == 0: continue

  if op == "*":
    sum *= num
  else:
    sum += num

print(sum + count)
  
