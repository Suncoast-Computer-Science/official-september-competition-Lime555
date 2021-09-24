l = []
for i in range(int(input())):
  l += [int(input())]
addl = []
for i in range(0, len(l), 2):
  addl += [l[i] + l[i + 1]]
print(addl)
for i in range(1, len(addl)):
  for j in range(i):
    if(addl[j] > addl[i]):
      x = addl[i]
      addl[i] = addl[j]
      addl[j] = x
print(addl)
