def liste(a, u):
    fruits = ["pomme","cerise", "orange", "melon"]
    fruits.insert(int(a), str(u))
    return fruits

x = input("Entrez l'index dans lequel ajouter le string: ")
b = input("Entrez l'élément à ajouter: ")
print(liste(x, b))