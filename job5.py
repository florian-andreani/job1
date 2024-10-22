def liste():
    entiers = [1, 2, 3, 4, 5]
    print(entiers)
    print(entiers[1])
    entiers[3] = entiers[2] + entiers[4]
    a = entiers[3]
    entiers.pop(3)
    entiers.insert(3, a)
    print(entiers)
    print(entiers[4])

liste()