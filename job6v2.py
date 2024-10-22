entiers = [1, 2, 3, 4, 5]
copy = entiers.copy()
entiers[0] = copy[-1]
entiers[-1] = copy[0]
print(entiers)