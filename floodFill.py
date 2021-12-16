from collections import deque 


def is_valid(i, j, image): 

    I = len(image) 
    J = len(image[0])

    if (0 <= i < I) and (0 <= j < J): 
        return True

    return False  


def valid_neighbors(i, j, image): 

    neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
    out = list() 

    for n in neighbors: 
        if is_valid(n[0], n[1], image): 
            out.append(n)

    return out 


def floodFill(image, sr, sc, newColor): 

    target_color = image[sr][sc]

    fringe = deque() 
    fringe.append((sr, sc))
    visited = set() 

    while fringe: 

        curr = fringe.pop() 
        visited.add(curr) 

        if image[curr[0]][curr[1]] == target_color: 
            image[curr[0]][curr[1]] = newColor

            neighbors = valid_neighbors(curr[0], curr[1], image) 
            for neigh in neighbors: 
                if (image[neigh[0]][neigh[1]] == target_color) and (neigh not in visited): 
                    fringe.append(neigh)

    return image 





if __name__ == '__main__':
    
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newColor = 2
    
    print(floodFill(image, sr, sc, newColor)) 