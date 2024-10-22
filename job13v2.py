def tri_doublons(liste_initiale, liste_comparée):

    for i in range(len(liste_initiale)):
                if liste_initiale[i] not in liste_comparée:
                 liste_comparée += [0]
                 liste_comparée[len(liste_comparée)-1] = liste_initiale[i]
    return liste_comparée

liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
liste_trie = []
           
print(tri_doublons(liste, liste_trie))
