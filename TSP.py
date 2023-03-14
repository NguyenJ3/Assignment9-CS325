def solve_tsp(G):
    n = len(G)

    #first node
    path = [0]
    for _ in range(n-1):

        #need to get the current node 
        curr = path[-1] 
        next_node = min(range(n), key=lambda x: G[curr][x] if x not in path else float('inf'))
        #appends nearest node 
        path.append(next_node)
        
    path.append(0)
    return path