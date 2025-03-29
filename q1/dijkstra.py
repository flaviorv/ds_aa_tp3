class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 not in self.adjacency_list:
            self.adjacency_list[vertex1] = []
        self.adjacency_list[vertex1].append((vertex2, weight))

    def dijkstra(self, origin, destination):
        unvisited = list(self.adjacency_list.keys())
        weights = {vertex: float("inf") for vertex in self.adjacency_list}
        weights[origin] = 0
        predecessors = {}
        while unvisited:
            current = min(unvisited, key=lambda vertex: weights[vertex])
            if weights[current] == float("inf"):
                break
            for neighbor in self.adjacency_list[current]:
                vertex, weight = neighbor[0], neighbor[1]
                new_weight = weights[current] + weight
                if new_weight < weights[vertex]:
                    weights[vertex] = new_weight
                    predecessors[vertex] = current
            unvisited.remove(current)
        path = []
        current = destination
        while current in predecessors.keys():
            path.insert(0, (current, weights[current]))
            current = predecessors[current]
        path.insert(0, (origin, 0))
        return path
    
    def show(self):
        for vertex in self.adjacency_list:
            print(vertex, self.adjacency_list[vertex])

    def min_path(self, origin, destination):
        path = self.dijkstra(origin, destination)
        print(path)
        if len(path) <= 1:
            print("Path not found")
        else:
            print(f"\nShortest Path Found Between {origin} and {destination}")
            for i in range(len(path)):
                if i != len(path)-1:
                    print(path[i], end="=>")
                else:
                    print(path[i], f"\nTotal distance: {path[i][1]}")

if __name__ == "__main__":
    print("Graph")
    g1 = Graph()
    e1 = [
        ("Downtown", "Warehouse 1", 2), ("Downtown", "Warehouse 2", 5), ("Downtown", "Neighborhood A", 3),
        ("Warehouse 1", "Downtown", 2), ("Warehouse 1", "Neighborhood B", 4), ("Warehouse 1", "Neighborhood C", 1),
        ("Warehouse 2", "Downtown", 5), ("Warehouse 2", "Warehouse 4", 2), ("Warehouse 2", "Neighborhood D", 6),
        ("Warehouse 3", "Warehouse 1", 3), ("Warehouse 3", "Neighborhood E", 2), ("Warehouse 3", "Neighborhood F", 5),
        ("Warehouse 4", "Warehouse 2", 2), ("Warehouse 4", "Neighborhood G", 3), ("Warehouse 4", "Warehouse 5", 4),
        ("Warehouse 5", "Warehouse 4", 4), ("Warehouse 5", "Neighborhood H", 2), ("Warehouse 5", "Neighborhood I", 3),
        ("Neighborhood A", "Downtown", 3), ("Neighborhood A", "Neighborhood B", 1), ("Neighborhood A", "Neighborhood C", 2),
        ("Neighborhood B", "Warehouse 1", 4), ("Neighborhood B", "Neighborhood A", 1), ("Neighborhood B", "Neighborhood D", 3),
        ("Neighborhood C", "Warehouse 1", 1), ("Neighborhood C", "Neighborhood A", 2), ("Neighborhood C", "Neighborhood E", 4),
        ("Neighborhood D", "Warehouse 2", 6), ("Neighborhood D", "Neighborhood B", 3), ("Neighborhood D", "Neighborhood F", 2),
        ("Neighborhood E", "Warehouse 3", 2), ("Neighborhood E", "Neighborhood C", 4), ("Neighborhood E", "Neighborhood G", 5),
        ("Neighborhood F", "Warehouse 3", 5), ("Neighborhood F", "Neighborhood D", 2), ("Neighborhood F", "Neighborhood H", 3),
        ("Neighborhood G", "Warehouse 4", 3), ("Neighborhood G", "Neighborhood E", 5), ("Neighborhood G", "Neighborhood I", 1),
        ("Neighborhood H", "Warehouse 5", 2), ("Neighborhood H", "Neighborhood F", 3), ("Neighborhood H", "Neighborhood J", 4),
        ("Neighborhood I", "Warehouse 5", 3), ("Neighborhood I", "Neighborhood G", 1), ("Neighborhood I", "Neighborhood J", 2),
        ("Neighborhood J", "Neighborhood H", 4), ("Neighborhood J", "Neighborhood I", 2), ("Warehouse 1", "Warehouse 3", 3)
    ]

    [g1.add_edge(ori, des, dis) for ori, des, dis in e1]
    g1.show()
    g1.min_path("Warehouse 1", "Neighborhood F")