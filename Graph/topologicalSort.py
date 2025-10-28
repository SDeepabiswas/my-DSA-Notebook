def topoSortUtil(v, adj, visited, stack):
    #  this function will basically perform the dfs to do tsort

    # MARK curr AS VISITED
    visited[v] = True

    # for all the adjacent vertices

    for neigh_v in adj[v]:
        if not visited[neigh_v]:
            topoSortUtil(neigh_v, adj, visited, stack)
    

    # PUSH THE NODE INTO THE STACK

    stack.append(v)

# FROM GIVEN INPUT MAKE AN ADJACENT MATRIX

def constructAdj(V, edges):
    adj = [[] for _ in range (V)]

    for edge in edges:
        adj[edge[0]].append(edge[1])
    
    return adj

# ACTUAL TOPOLOGICAL SORT ALGO

def topologicalSort(V, edges):
    stack = []
    visited = [False] * V

    adj = constructAdj(V, edges)

    for i in range(V):
        if not visited[i]:
            topoSortUtil(i, adj, visited, stack)
    
    return stack[::-1]

if __name__ == "__main__":
    v=6
    
    # representing graph by adjacency list

    edges = [[2,3],[3,1],[4,0],[4,1],[5,0],[5,2]]

    print(topologicalSort(v,edges))
    # print(" ".join(map(str, ans)))
