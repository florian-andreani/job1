liste = [2, 1, 5, 3, 4]

def croissant(liste_a_trier):
    x = 0  
    while x < 4:
            i = 0
            while i < 4:
                if liste_a_trier[i] > liste_a_trier[i+1]:
                    liste_a_trier[i], liste_a_trier[i+1] = liste_a_trier[i+1], liste_a_trier[i] 
                x += 1
                i += 1 
                 
croissant(liste)
print(liste)
