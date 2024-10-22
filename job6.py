entiers = [1, 2, 3, 4, 5]
entiers_rev = entiers[::-1]
x = entiers_rev[0]
y = entiers_rev[4]
entiers.pop(0)
entiers.pop(3)
entiers.insert(0, x)
entiers.insert(4, y)
print(entiers)