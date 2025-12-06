file = open('input.txt', 'r')
lines = [l.strip() for l in file.readlines()]
lines = [l.split() for l in lines]

count = 0

for i in range(len(lines[0])):
  op = lines[-1][i]
  sum = 1 if op == "*" else 0
  for j in range(len(lines) - 1):
    if op == "*":
      sum *= int(lines[j][i])
    else:
      sum += int(lines[j][i])
  count += sum

print(count)
