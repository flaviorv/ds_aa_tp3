def floyd_warshall(graph):
    length = len(graph)
    for k in range(length):
        for i in range(length):
            for j in range(length):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    return graph

if __name__ == "__main__":
    INF = float('inf')
    neighborhoods = [
        [0, 3, INF, 7, INF],
        [3, 0, 2, INF, INF],
        [INF, 2, 0, 5, 1],
        [7, INF, 5, 0, 2],
        [INF, INF, 1, 2, 0]
    ]
    paths = floyd_warshall(neighborhoods)
    print("Path with lower time:")
    for neighborhood1 in range(len(paths)):
        for neighborhood2 in range(len(paths)):
            print(f"From N{neighborhood1+1} to N{neighborhood2+1}: {paths[neighborhood1][neighborhood2]}min")
        

