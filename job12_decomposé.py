liste = [2, 1, 5, 3, 4]
def croissant(x):
    for x in range(0, 5): 
        for i in range(x+1, 5): 
            if liste[x] > liste[i]:
                liste[x], liste[i] = liste[i], liste[x] 
            else : 
                for i in range(x+2, 5): 
                    if liste[x] > liste[i]:
                        liste[x], liste[i] = liste[i], liste[x] 
                    else: 
                        for i in range(x+3, 5): 
                            if liste[x] > liste[i]:
                                liste[x], liste[i] = liste[i], liste[x] 
                            for i in range(x+4, 5): 
                                    if liste[x] > liste[i]:
                                        liste[x], liste[i] = liste[i], liste[x] 
            
        
x = 0    
croissant(x)
print(liste)
