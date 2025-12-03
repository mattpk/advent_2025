file = open('input.txt', 'r')
all_lines = file.readlines()
sum = 50
count = 0
for raw_line in all_lines:
  line = raw_line.strip()
  sum += int(line[1:]) * (-1 if line[0] == 'L' else 1)
  if (sum % 100 == 0):
    count += 1
print(count)
