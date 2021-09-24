stars = int(input())
output = ""
for num in range(1, stars + 1, 2):
  half = int((num + 1) / 2)
  for i in range(half):
    for space in range(half - i - 1):
      output += " "
    for star in range((i + 1) * 2 - 1):
      output += "*"
    print(output)
    output = ""
  for i in range(half - 1, 0, -1):
    for space in range(num - i - half + 1):
      output += " "
    for star in range(i * 2 - 1):
      output += "*"
    print(output)
    output = ""
  print(" ")
for num in range(stars - 1, 1, -2):
  half = int((num + 1) / 2)
  for i in range(half):
    for space in range(half - i - 1):
      output += " "
    for star in range((i + 1) * 2 - 1):
      output += "*"
    print(output)
    output = ""
  for i in range(half - 1, 0, -1):
    for space in range(num - i - half):
      output += " "
    for star in range(i * 2 - 1):
      output += "*"
    print(output)
    output = ""
  print(" ")
