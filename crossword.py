parta = input()
partb = input()
wordlen = int(input())
output = ""
if(len(parta) > len(partb)):
  output += partb
  output += parta
else:
  output += parta
  output += partb
if(len(output) == wordlen):
  print(output)
else:
  print(False)
