def solve_tsp(G):
    n = len(G)
    #counters to track node 

    visited = [False] * n
    path = [0]
    visited[0] = True
    curr = 0

    
