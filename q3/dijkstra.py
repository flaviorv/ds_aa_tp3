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
            print(f"\nShortest Path Found Between {origin} and {destination}")
            for i in range(len(path)):
                if i != len(path)-1:
                    print(path[i], end="=>")
                else:
                    print(path[i], f"\nTotal Distance (km): {path[i][1]}")

if __name__ == "__main__":
    print("Graph")
    g1 = Graph()
    e1 = [
        ("Airport A", "Airport B", 450), ("Airport A", "Airport C", 720),
        ("Airport B", "Airport A", 450), ("Airport B", "Airport D", 980), ("Airport B", "Airport E", 300),
        ("Airport C", "Airport A", 720), ("Airport C", "Airport D", 510), ("Airport C", "Airport F", 1300),
        ("Airport D", "Airport B", 980), ("Airport D", "Airport C", 510), ("Airport D", "Airport G", 750),
        ("Airport E", "Airport B", 300), ("Airport E", "Airport H", 420), ("Airport E", "Airport I", 1150),
        ("Airport F", "Airport C", 1300), ("Airport F", "Airport G", 290), ("Airport F", "Airport J", 890),
        ("Airport G", "Airport D", 750), ("Airport G", "Airport F", 290), ("Airport G", "Airport H", 500),
        ("Airport H", "Airport E", 420), ("Airport H", "Airport G", 500), ("Airport H", "Airport I", 700),
        ("Airport I", "Airport E", 1150), ("Airport I", "Airport H", 700), ("Airport I", "Airport J", 650),
        ("Airport J", "Airport F", 890), ("Airport J", "Airport I", 650)
    ]
    [g1.add_edge(ori, des, dis) for ori, des, dis in e1]
    g1.show()
    g1.min_path("Airport I", "Airport C")