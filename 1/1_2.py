file = open('input.txt', 'r')
all_lines = file.readlines()
sum = 50
count = 0

def num_times_crosses_100(start, end):
  if (start > end):
    # ceil using upside-down floor division
    return -(start // -100 - end // -100)
  return end // 100 - start // 100

for raw_line in all_lines:
  line = raw_line.strip()
  turn = int(line[1:])
  sign = -1 if line[0] == 'L' else 1
  next = sum + turn * sign
  count += num_times_crosses_100(sum, next)
  sum = next
print(count)
