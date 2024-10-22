
liste2 = []
liste = [7, 11, 42, 39, 2]

def augment(radis):
    for i in liste:
        liste2.append(i+1)


augment(liste)
liste = liste2
print(liste)
        