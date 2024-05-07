def search_in_2d_array(array: [[int]], nb: int) -> (int, int):
    n=len(array) 
    m=len(array[0]) 
    for i in range(n):
        for j in range(m):
            if array[i][j] == nb:
                return(i,j)
    else:
      return(-1,-1)    
    

