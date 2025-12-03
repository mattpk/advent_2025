file = open('input.txt', 'r')
lines = [l.strip() for l in file.readlines()]
sum = 0
for line in lines:
  max = int(line[-2])
  sec = int(line[-1])
  for char in line[:-1]:
    n = int(char)
    if n > max:
      max = n
      sec = int(line[-1])
    elif n > sec:
      sec = n
  sum += max * 10 + sec
print(sum)
