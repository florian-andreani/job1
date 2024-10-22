def croissant(rideau):
    for x in range(0, 4): 
        for i in range(0, 4): 
            if liste[i] > liste[i+1]:
                liste[i], liste[i+1] = liste[i+1], liste[i] 

    return rideau 

liste = [2, 1, 5, 3, 4]

croissant(liste)
print(liste)
