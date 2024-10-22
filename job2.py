def liste(a):
    fruits = ["pomme", "cerise", "orange"]
    return fruits[int(a)]


b = input("Quel index voulez vous imprimer ? : ")
print(liste(b))