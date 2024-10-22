def liste(a):
    fruits = ["pomme", "cerise", "orange"]
    fruits.append(str(a))
    return fruits

b = input("Entrez l'élément à ajouter: ")
print(liste(b))