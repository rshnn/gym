
import numpy as np 

def is_valid(i, j, grid): 

    m, n = len(grid), len(grid[0])

    if (0 <= i < m) and (0 <= j < n): 
        return True
    else:
        return False 

def first_pass_neighbors(i, j, grid): 
    """ Returns top and left 
    """
    top = (i-1, j) 
    left = (i, j-1)

    return (top if is_valid(top[0], top[1], grid) else None, 
            left if is_valid(left[0], left[1], grid) else None)  

def second_pass_neighbors(i, j, grid): 
    """ Returns bottom and right  
    """
    bottom = (i+1, j) 
    right = (i, j+1)

    return (bottom if is_valid(bottom[0], bottom[1], grid) else None, 
            right if is_valid(right[0], right[1], grid) else None)  



def orangesRotting(grid): 
    
    m, n = len(grid), len(grid[0])
    dummy_grid = [[None for i in range(n)] for j in range(m)]


    # First pass.  
    for i in range(m): 
        for j in range(n): 

            if grid[i][j] == 2: 
                dummy_grid[i][j] = 0 
                continue 

            if grid[i][j] == 0: 
                dummy_grid[i][j] = None  
                continue 


            # normal orange 
            # put in min(top, bottom) + 1 

            neighbors = first_pass_neighbors(i, j, grid) 
            vals = list() 
            for nei in neighbors: 
                if nei and dummy_grid[nei[0]][nei[1]] != None: 
                    vals.append(dummy_grid[nei[0]][nei[1]]) 


            if len(vals) == 0: 
                dummy_grid[i][j] = np.inf 
            else: 
                dummy_grid[i][j] =  min(vals) + 1 



    print_grid(dummy_grid)  

    # second pass 
    max_so_far = 0 

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1): 

            if grid[i][j] == 2: 
                dummy_grid[i][j] = 0 
                continue 

            if grid[i][j] == 0: 
                dummy_grid[i][j] = None  
                continue 


            # normal orange 
            # put in min(top, bottom) + 1 

            neighbors = second_pass_neighbors(i, j, grid) 
            vals = list() 
            for nei in neighbors: 
                if nei and dummy_grid[nei[0]][nei[1]] != None: 
                    vals.append(dummy_grid[nei[0]][nei[1]]) 


            if len(vals) == 0: 
                pass  
            else: 
                dummy_grid[i][j] = min(dummy_grid[i][j], min(vals) + 1) 


            # if dummy_grid[i][j] == np.inf: 
            #     return -1 


            max_so_far = max(max_so_far, dummy_grid[i][j])


    print()
    print_grid(dummy_grid)  
    return max_so_far


def print_grid(grid): 
    for i in grid: 
        print(i)
            

if __name__ == "__main__":

    # grid_1 = [[1, 0, 1, 1],
    #         [0, 1, 0, 1],
    #         [2, 0, 1, 2],
    #         [1, 1, 1, 1]]

    # grid = [[2,1,1],[0,1,1],[1,0,1]]

    # grid = [[0,2]]

    # grid = [[2,1,1],[1,1,0],[0,1,1]]

    grid = [[2,0,1,1,1,1,1,1,1,1],
            [1,0,1,0,0,0,0,0,0,1],
            [1,0,1,0,1,1,1,1,0,1],
            [1,0,1,0,1,0,0,1,0,1],
            [1,0,1,0,1,0,0,1,0,1],
            [1,0,1,0,1,1,0,1,0,1],
            [1,0,1,0,0,0,0,1,0,1],
            [1,0,1,1,1,1,1,1,0,1],
            [1,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1]]


    print(orangesRotting(grid) )   




    
    
    
    # print(first_pass_neighbors(0, 1, grid))

