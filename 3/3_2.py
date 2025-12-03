file = open('input.txt', 'r')
lines = [l.strip() for l in file.readlines()]
sum = 0
for line in lines:
  num = ""
  prev = -1
  enumerated = list(enumerate(line))
  for i in range(12):
    best = max(enumerated[prev+1:len(line)-11 + i], key=lambda v: v[1])
    num = num + best[1]
    prev = best[0]
  sum += int(num)
print(sum)
