



def is_valid(i, j, matrix): 
    """Returns true if i, j is valid within matrix bounds 
    """


    n, m = len(matrix), len(matrix[0])

    if (0<= i < n) and (0<=j < m): 
        return True 
    else: 
        return False 


def valid_neighbors(i, j, matrix): 
    """ Returns valid cardinal neighbors 
    """
    neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
    out = [] 

    for neigh in neighbors: 
        if is_valid(neigh[0], neigh[1], matrix): 
            out.append(neigh) 

    return out  



def is_border(tmp, matrix): 
    return (tmp[0] == 0) or (tmp[0] == len(matrix)-1) or (tmp[1] == 0) or (tmp[1] == len(matrix[0])-1) 




from collections import deque 

def bfs_on_island_candidate(i, j, matrix, visited): 

    found_border_path = False 

    queue = deque() 
    revisit = deque() 

    queue.append((i, j)) 
    revisit.append((i, j)) 

    while queue: 
        
        tmp = queue.popleft() 
        visited.add(tmp) 

        # is it an border island 
        if is_border(tmp, matrix): 
            found_border_path = True 

        # add neighbors 
        neighbors = valid_neighbors(tmp[0], tmp[1], matrix)  
        for neigh in neighbors: 
            if (neigh not in visited) and (matrix[neigh[0]][neigh[1]] == 1):  
                queue.append(neigh) 
                revisit.append(neigh)  


    # if i did not find a border path, set all 1s visited to 0  
    if not found_border_path: 
        for item in list(revisit): 
            matrix[item[0]][item[1]] = 0 

    return 




def removeIslands(matrix):
    # Write your code here.

    if not matrix: 
        return None 

    if len(matrix[0]) < 1: 
        return None 

    n, m = len(matrix), len(matrix[0])

    # keep track of visited  
    visited = set() 

    # iterate through middle square 
    for i in range(1, n-1): 
        for j in range(1, m-1): 

            if (i, j) in visited:
                continue  
            visited.add((i, j))
            # run bfs on candidate islands to search for edge 1 
            if matrix[i][j] == 1: 
                bfs_on_island_candidate(i, j, matrix, visited) 



    return matrix

mat = [
  [1, 0, 0, 0, 0, 0],
  [0, 1, 0, 1, 1, 1],
  [0, 0, 1, 0, 1, 0],
  [1, 1, 0, 0, 1, 0],
  [1, 0, 1, 1, 0, 0],
  [1, 0, 0, 0, 0, 1]
]


new_matrix = removeIslands(mat)

for i in new_matrix: 
    print(i)