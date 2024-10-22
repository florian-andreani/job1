liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
liste_trie = []

def tri_doublons(liste_initiale, liste_comparée):
        i = 0
        while i < (compteur_liste(liste_initiale)):
          if liste_initiale[i] not in liste_comparée:
           liste_comparée += [0]
           liste_comparée[(compteur_liste(liste_comparée))-1] = liste_initiale[i]
          i += 1
        return liste_comparée

def compteur_liste(liste_comptée):
    compteur = 0
    for i in liste_comptée:
        compteur += 1
    return compteur

print(tri_doublons(liste, liste_trie))