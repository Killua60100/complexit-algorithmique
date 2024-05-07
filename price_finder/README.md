
explications linéaire de l'algorithme:

création de deux variables price_min et price_max a 1 et 500
definition de la fonction price avec une variable de types int nommé price 
si price est inférieur a price min et supérieur a price_max 
alors retourner -1
créations de la variable arr qui est une liste de nombre price_min jusqu'a price max 
créations de la variable found et lui assignier -1
tant que found est différent de price ->
création de la variable size qui compte la longueur de arr 
création de la variable index qui va prend size, le divisé par deux, et prendre le plus grand entier en dessous du résultat si le résulat n'est pas un entier 
found devient le nombre de la position index dans la liste 
si la nouvelle valeur de found est inférieur a price 
on supprime toute la partie inférieur de la liste arr avec index valeur 
sinon
on supprime toute la partie supérieur de la liste arr avec index valeur 
renvoie found 



explication générale: 

cette aglo travail sur une valeur qu'on donne en variable nommé price, si la valeur n'est pas entre 1 et 500 compris 
l'algo renvoie la valeur -1, si la valeur est compris dans cette intervale, il va créer une liste nommé arr de 1 jusqu'a 500 et
trouver cette meme valeur dans la liste de facon dicothomique soit avec une compléxité logarithmique.

cette méthode consiste a ciblé la valeur du milieu de la liste, si cette valeur est supérieur a la valeur recherché
alors cette meme valeur prend la place de la valeur maxi, et dans le cas inverse, si cette valeur est plus petit 
que la valeur cherché alors il prend la place de la valeur min

complexité de l'argotithme:
logaritmique O (log(n))