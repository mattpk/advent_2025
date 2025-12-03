file = open('input.txt', 'r')
sum = 0
for r in file.readline().strip().split(','):
  pair = r.split('-')
  for i in range(int(pair[0]), int(pair[1]) + 1):
    length = len(str(i))
    for j in range(1, length // 2+1):
      if (length % j == 0 and str(i) == (str(i)[0:j] * (length // j))):
        sum += i
        # print(i)
        break
print(sum)