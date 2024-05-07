ce programe prend en paramètre une liste bidimensionelle qui contient donc plusieurs liste dans une liste
et prend en compte un nombre nb et le recherche dans la liste afin de retourner sa position

écrire "python3 solution.py" pour lancer le programme 

compléxité de l'agorithme : 

    O (n²) quadratique 
    car il y a une boucle dans une boucle 

test de l'algorithme : 

array: [[int]] = [[3,1,4],[5,2,7],[6,9,8]]
print (search_in_2d_array(array, 9 ))