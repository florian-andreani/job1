def compteur(liste_comptée):
    compt = 0
    for i in liste_comptée:
        compt += 1
    return compt

def croissant(liste_a_trier, nombredentiers):
    x = 0  
    while x < nombredentiers:
            i = 0
            while i < (nombredentiers)-1:
                if liste_a_trier[i] > liste_a_trier[i+1]:
                    liste_a_trier[i], liste_a_trier[i+1] = liste_a_trier[i+1], liste_a_trier[i] 
                i += 1
            x += 1
             
def arrondissement(liste_nombres):
    i = 0
    while i < compteur(liste_nombres):
        liste_nombres[i] + 0.5
        liste_nombres[i] = (int(liste_nombres[i]))
        i += 1
    return liste_nombres

liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]


arrondissement(liste)
croissant(liste, compteur(liste))
print(liste)


