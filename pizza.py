slices = int(input())
party = int(input())
family = int(input())
print(((slices % party) % family) == 0)
