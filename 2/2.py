file = open('input.txt', 'r')
sum = 0
for r in file.readline().strip().split(','):
  pair = r.split('-')
  for i in range(int(pair[0]), int(pair[1]) + 1):
    length = len(str(i))
    if length % 2 == 0 and str(i)[0:length // 2] == str(i)[length // 2:]:
      sum += i
      # print(i)
print(sum)