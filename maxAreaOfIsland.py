

from collections import deque 


def is_valid(i, j, grid): 

    I = len(grid) 
    J = len(grid[0])

    if (0 <= i < I) and (0 <= j < J): 
        return True

    return False  


def valid_neighbors(i, j, grid): 

    neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
    out = list() 

    for n in neighbors: 
        if is_valid(n[0], n[1], grid): 
            out.append(n)

    return out 




def traverse_island(i, j, grid, visited): 

    fringe = deque()
    fringe.append((i, j))
    area = 0 

    while fringe: 

        curr = fringe.pop() 

        if curr in visited: 
            continue 

        visited.add(curr) 
        area += 1 

        neighbors = valid_neighbors(curr[0], curr[1], grid)  

        for neigh in neighbors: 
            if (grid[neigh[0]][neigh[1]] == 1) and (neigh not in visited): 
                fringe.append(neigh)


    return area 



def maxAreaOfIsland(grid): 
    

    visited = set() 
    largest_area = 0 

    for i in range(len(grid)): 
        for j in range(len(grid[i])): 

            if grid[i][j] == 1: 
                area = traverse_island(i, j, grid, visited) 

                if area > largest_area: 
                    largest_area = area 

    return largest_area 



if __name__ == '__main__':
    
    grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
    print(maxAreaOfIsland(grid))  