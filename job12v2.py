liste = [2, 1, 5, 3, 4]

def croissant(x):
    for x in range(len(liste)): #Pour chaque les éléments jusqu'a la fin de la liste
        for i in range(x+1, len(liste)): #Pour chaque élément de l'élément suivant jusqu'a la fin de la liste
            if liste[x] > liste[i]: #Si l'élément est plus grand
                liste[x], liste[i] = liste[i], liste[x] #Echange les
            else: continue #Sinon passe au suivent
        
x = 0    
croissant(x)
print(liste)