class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, vertex1, vertex2, distance):
        if vertex1 not in self.adjacency_list:
            self.adjacency_list[vertex1] = []
        self.adjacency_list[vertex1].append((vertex2, distance))

    def dijkstra(self, origin, destination):
        unvisited = list(self.adjacency_list.keys())
        distances = {vertex: float("inf") for vertex in self.adjacency_list}
        distances[origin] = 0
        predecessors = {}
        while unvisited:
            current = min(unvisited, key=lambda vertex: distances[vertex])
            if distances[current] == float("inf"):
                break
            for neighbor in self.adjacency_list[current]:
                vertex, distance = neighbor[0], neighbor[1]
                new_distance = distances[current] + distance
                if new_distance < distances[vertex]:
                    distances[vertex] = new_distance
                    predecessors[vertex] = current
            unvisited.remove(current)
        path = []
        current = destination
        while current in predecessors.keys():
            path.insert(0, (current, distances[current]))
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
            print(f"\nFaster Path Found Between {origin} and {destination}")
            for i in range(len(path)):
                if i != len(path)-1:
                    print(path[i], end="=>")
                else:
                    print(path[i], f"\nAverage time (hours): {path[i][1]}")

if __name__ == "__main__":
    print("Graph")
    g1 = Graph()
    e1 = [
        ("Neighborhood A", "Neighborhood B", 2), ("Neighborhood A", "Neighborhood C", 3),
        ("Neighborhood B", "Neighborhood A", 2), ("Neighborhood B", "Neighborhood D", 4), ("Neighborhood B", "Neighborhood E", 1),
        ("Neighborhood C", "Neighborhood A", 3), ("Neighborhood C", "Neighborhood D", 2), ("Neighborhood C", "Neighborhood F", 5),
        ("Neighborhood D", "Neighborhood B", 4), ("Neighborhood D", "Neighborhood C", 2), ("Neighborhood D", "Neighborhood G", 3),
        ("Neighborhood E", "Neighborhood B", 1), ("Neighborhood E", "Neighborhood H", 2), ("Neighborhood E", "Neighborhood I", 4),
        ("Neighborhood F", "Neighborhood C", 5), ("Neighborhood F", "Neighborhood G", 1), ("Neighborhood F", "Neighborhood J", 3),
        ("Neighborhood G", "Neighborhood D", 3), ("Neighborhood G", "Neighborhood F", 1), ("Neighborhood G", "Neighborhood H", 2),
        ("Neighborhood H", "Neighborhood E", 2), ("Neighborhood H", "Neighborhood G", 2), ("Neighborhood H", "Neighborhood I", 3),
        ("Neighborhood I", "Neighborhood E", 4), ("Neighborhood I", "Neighborhood H", 3), ("Neighborhood I", "Neighborhood J", 2),
        ("Neighborhood J", "Neighborhood F", 3), ("Neighborhood J", "Neighborhood I", 2)
    ]

    [g1.add_edge(ori, des, dis) for ori, des, dis in e1]
    g1.show()
    g1.min_path("Neighborhood J", "Neighborhood D")