def compteur(liste_comptée):
    compteur = 0
    for i in liste_comptée:
        compteur += 1
    return compteur


def my_long_word(a, chaine):
    
    liste = chaine.split()
    index_mot = 0
    i = 0
    while i < compteur(liste):
        if a < compteur(liste[index_mot]):
           mots_triés.append(liste[index_mot])
        i +=1
        index_mot += 1
    return mots_triés

mots_triés = []
phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"

print(my_long_word(3, phrase))
