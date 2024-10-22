
def compteur_liste(liste_comptée):
    compteur = 0
    for i in liste_comptée:
        compteur += 1
    return compteur
           
liste_comparée = []
for i in [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]:
    if [i] not in liste_comparée:
        liste_comparée += [0]
        liste_comparée[compteur_liste(liste_comparée)-1] = [i]

print(liste_comparée)

