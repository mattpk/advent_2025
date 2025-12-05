file = open('input.txt', 'r')
lines = [l.strip() for l in file.readlines()]
blank_index = lines.index("")
count = 0
for num in lines[blank_index+1:]:
  for i, j in [l.split('-') for l in lines[:blank_index]]:
    if int(i) <= int(num) <= int(j):
      count+= 1
      break
print(count)
