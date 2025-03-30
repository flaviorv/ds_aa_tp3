class Graph:
    def __init__(self):
        self.adjacency_list = {}

    #now, weight is a tuple with 3 values (distance, average_time, charging_station)
    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 not in self.adjacency_list:
            self.adjacency_list[vertex1] = []
        self.adjacency_list[vertex1].append((vertex2, weight))
        if vertex2 not in self.adjacency_list:
            self.adjacency_list[vertex2] = []
        self.adjacency_list[vertex2].append((vertex1, weight))

    #the algorithm takes into account the vehicle's autonomy and does not return a path that it cannot complete
    def dijkstra(self, origin, destiantion, autonomy):
        unvisited = list(self.adjacency_list.keys())
        weights = {vertex: (None, float("inf")) for vertex in self.adjacency_list}
        weights[origin] = (0, 0, False, autonomy) 
        predecessors = {}
        while unvisited:
            current = min(unvisited, key=lambda vertex: weights[vertex][1])
            if weights[current][1] == float("inf"):
                break
            for neighbor in self.adjacency_list[current]:
                nvertex, weight = neighbor[0], neighbor[1]
                ndistance = weight[0]
                ntime = weight[1]
                charging_station = weight[2]
                path_autonomy = weights[current][3]
                path_distance = weights[current][0] + ndistance
                path_time = weights[current][1] + ntime
                path_autonomy -= ndistance
                if path_autonomy > 0:
                    if path_time < weights[nvertex][1] or \
                    (path_time == weights[nvertex][1] and path_distance < weights[nvertex][0]):
                        if charging_station:
                            path_autonomy = autonomy
                        weights[nvertex] = (path_distance, path_time, charging_station, path_autonomy)
                        predecessors[nvertex] = current
            unvisited.remove(current)
        path = []
        current = destiantion
        while current in predecessors.keys():
            path.insert(0, (current, weights[current]))
            current = predecessors[current]
        path.insert(0, (origin, weights[origin]))
        return path

    def show_graph(self, detailed=False):
        print("Graph")
        for vertex in self.adjacency_list:
            if detailed:
                print(vertex, self.adjacency_list[vertex])
            else:
                print(vertex, [neighbor for neighbor, weight in self.adjacency_list[vertex]])

    def show_path(self, origin, destination, autonomy):
        path = self.dijkstra(origin, destination, autonomy)
        if len(path) <= 1:
            print("Path not found")
        else:
            print(f"Best Path Found Between {origin} and {destination}")
            for i in range(len(path)):
                print(f'{path[i][0]} time: {path[i][1][1]}min distance: {path[i][1][0]}km autonomy: {path[i][1][3]}km' \
                    f'{' - charging station' if path[i][1][2] else ""} {'=>' if i != len(path)-1 else "- arrival"}')
                    
if __name__ == "__main__":
    
    edges = [
        ("Intersection 1", "Intersection 2", (18, 14, False)),
        ("Intersection 1", "Intersection 5", (25, 18, True)),
        ("Intersection 1", "Intersection 3", (22, 15, False)),
        
        ("Intersection 2", "Intersection 6", (30, 22, False)),
        ("Intersection 2", "Intersection 3", (24, 17, True)),
        ("Intersection 2", "Intersection 7", (20, 13, False)),
        
        ("Intersection 3", "Intersection 4", (28, 20, False)),
        ("Intersection 3", "Intersection 8", (21, 11, True)),
        
        ("Intersection 4", "Intersection 9", (27, 17, False)),
        ("Intersection 4", "Intersection 10", (35, 24, False)),
        ("Intersection 4", "Intersection 5", (23, 16, False)),
        
        ("Intersection 5", "Intersection 6", (15, 10, False)),
        ("Intersection 5", "Intersection 11", (18, 13, True)),
        
        ("Intersection 6", "Intersection 7", (19, 14, True)),
        ("Intersection 6", "Intersection 12", (12, 7, False)),
        ("Intersection 6", "Intersection 8", (22, 15, False)),
        
        ("Intersection 7", "Intersection 13", (28, 20, False)),
        ("Intersection 7", "Intersection 8", (25, 18, True)),
        
        ("Intersection 8", "Intersection 14", (21, 11, True)),
        ("Intersection 8", "Intersection 9", (26, 18, False)),
        
        ("Intersection 9", "Intersection 15", (26, 16, False)),
        ("Intersection 9", "Intersection 10", (30, 21, False)),
        
        ("Intersection 10", "Intersection 16", (30, 21, True)),
        ("Intersection 10", "Intersection 11", (19, 12, False)),
        
        ("Intersection 11", "Intersection 17", (18, 13, False)),
        ("Intersection 11", "Intersection 12", (24, 15, True)),
        
        ("Intersection 12", "Intersection 18", (24, 15, False)),
        ("Intersection 12", "Intersection 13", (22, 14, True)),
        
        ("Intersection 13", "Intersection 19", (22, 14, True)),
        ("Intersection 13", "Intersection 14", (20, 11, False)),
        
        ("Intersection 14", "Intersection 20", (27, 18, False)),
        ("Intersection 14", "Intersection 15", (25, 16, False)),
        
        ("Intersection 15", "Intersection 21", (23, 13, False)),
        ("Intersection 15", "Intersection 16", (28, 20, False)),
        
        ("Intersection 16", "Intersection 22", (29, 19, False)),
        ("Intersection 16", "Intersection 17", (30, 21, True)),
        
        ("Intersection 17", "Intersection 23", (20, 12, True)),
        ("Intersection 17", "Intersection 18", (22, 13, False)),
        
        ("Intersection 18", "Intersection 24", (25, 17, False)),
        ("Intersection 18", "Intersection 19", (28, 19, True)),
        
        ("Intersection 19", "Intersection 25", (28, 20, False)),
        ("Intersection 19", "Intersection 20", (30, 22, True)),
        
        ("Intersection 20", "Intersection 26", (30, 22, True)),
        ("Intersection 20", "Intersection 21", (27, 17, False)),
        
        ("Intersection 21", "Intersection 27", (31, 21, False)),
        ("Intersection 21", "Intersection 22", (29, 19, False)),
        
        ("Intersection 22", "Intersection 28", (26, 15, False)),
        ("Intersection 22", "Intersection 23", (24, 16, False)),
        
        ("Intersection 23", "Intersection 29", (22, 14, False)),
        ("Intersection 23", "Intersection 24", (25, 17, False)),
        
        ("Intersection 24", "Intersection 30", (27, 18, False)),
        ("Intersection 24", "Intersection 25", (24, 16, False)),
        
        ("Intersection 25", "Intersection 31", (24, 16, False)),
        ("Intersection 25", "Intersection 26", (30, 22, True)),
        
        ("Intersection 26", "Intersection 32", (32, 23, False)),
        ("Intersection 26", "Intersection 27", (31, 21, False)),
        
        ("Intersection 27", "Intersection 33", (19, 14, False)),
        ("Intersection 27", "Intersection 28", (26, 15, True)),
        
        ("Intersection 28", "Intersection 34", (21, 12, False)),
        ("Intersection 28", "Intersection 29", (29, 18, False)),
        
        ("Intersection 29", "Intersection 35", (29, 18, False)),
        ("Intersection 29", "Intersection 30", (30, 22, False)),
        
        ("Intersection 30", "Intersection 36", (30, 22, False)),
        ("Intersection 30", "Intersection 31", (28, 19, False)),
        
        ("Intersection 31", "Intersection 37", (28, 19, False)),
        ("Intersection 31", "Intersection 32", (32, 23, False)),
        
        ("Intersection 32", "Intersection 38", (22, 15, True)),
        ("Intersection 32", "Intersection 33", (19, 14, True)),
        
        ("Intersection 33", "Intersection 39", (27, 17, False)),
        ("Intersection 33", "Intersection 34", (25, 15, False)),
        
        ("Intersection 34", "Intersection 40", (25, 15, False)),
        ("Intersection 34", "Intersection 35", (29, 18, False))
    ]

    graph = Graph()
    [graph.add_edge(ori, des, wei) for ori, des, wei in edges]
    # graph.show_graph(detailed=False)
    graph.show_path("Intersection 8", "Intersection 40", 50)








