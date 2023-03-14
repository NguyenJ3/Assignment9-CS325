def solve_tsp(G):
    n = len(G)

    #first node
    path = [0]
    for _ in range(n-1):

        #need to get the current node 
        curr = path[-1] 
        next_node = min((neighbor for neighbor in range(n) if G[curr][neighbor] > 0 and neighbor not in path),
            key=lambda x: G[curr][x])
        #appends nearest node 
        path.append(next_node)

    path.append(0)
    return path