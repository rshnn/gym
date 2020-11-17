def riverSizes(matrix):
    # Write your code here.
    
    sizes = list() 
    w = len(matrix)
    h = len(matrix[0])
    
    for i in range(w): 

        for j in range(h): 
            
            if matrix[i][j] == 1: 
                # It is part of a river 
                size, matrix = travel_river(i, j, matrix) 
                sizes.append(size) 

            else: 
                # It is not part of a river.  Move to next. 
                pass  

    return sizes     
            


def travel_river(i, j, matrix): 
    """ Travels along a river starting at point i, j and counts river size 
    """

    # mark position as visited 
    size = 1 
    matrix[i][j] = 2 

    fringe = check_neighbors(i, j, matrix)

    i = 0
    while(i < len(fringe)): 

        pos = fringe[i]
        if matrix[pos[0]][pos[1]] == 1: 
            # Mark position as visited 
            size += 1
            matrix[pos[0]][pos[1]] = 2 
            fringe = fringe + check_neighbors(pos[0], pos[1], matrix)


        # increment 
        i += 1



    return size, matrix 

            
def check_neighbors(i, j, matrix): 
    """ Checks neighbors of matrix[i, j] and returns indicies of all river nodes
    """
                       
    top = (i, j+1)
    bottom = (i, j-1)
    left = (i-1, j)
    right = (i+1, j)

    river_pts = list()


    for pos in [top, bottom, left, right]: 

        if is_valid(pos[0], pos[1], matrix): 
            if matrix[pos[0]][pos[1]] == 1: 
                river_pts.append(pos)

    return river_pts 


def is_valid(i, j, matrix): 
    """ Checks if position i, j is valid on the matrix 
    """

    w = len(matrix)
    h = len(matrix[0])
    
    if (0 <= i < w) and (0 <= j < h):
        return True 

    else: 
        return False 




def __print_matrix(matrix): 

    for row in matrix: 
        print(row)



if __name__ == "__main__":

    testInput = [[1, 0, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 0]]
    # expected = [1, 2, 2, 2, 5]
    
    sizes = riverSizes(testInput)
    print(sizes) 