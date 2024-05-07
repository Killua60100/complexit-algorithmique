def search_in_array(array: [int], nb: int) -> int : 
    n = len(array)
    for i in range (n):
        if array[i] == nb : 
            return i
    else :
     return -1


    