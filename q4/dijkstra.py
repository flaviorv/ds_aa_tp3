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
            print(f"\nLower Cost Path Found Between {origin} and {destination}")
            for i in range(len(path)):
                if i != len(path)-1:
                    print(path[i], end="=>")
                else:
                    print(path[i], f"\nFuel cost ($): {path[i][1]}")

if __name__ == "__main__":
    print("Graph")
    g1 = Graph()
    e1 = [
        ("City A", "City B", 350), ("City A", "City C", 520),
        ("City B", "City A", 350), ("City B", "City D", 740), ("City B", "City E", 220),
        ("City C", "City A", 520), ("City C", "City D", 410), ("City C", "City F", 860),
        ("City D", "City B", 740), ("City D", "City C", 410), ("City D", "City G", 620),
        ("City E", "City B", 220), ("City E", "City H", 330), ("City E", "City I", 800),
        ("City F", "City C", 860), ("City F", "City G", 270), ("City F", "City J", 570),
        ("City G", "City D", 620), ("City G", "City F", 270), ("City G", "City H", 420),
        ("City H", "City E", 330), ("City H", "City G", 420), ("City H", "City I", 550),
        ("City I", "City E", 800), ("City I", "City H", 550), ("City I", "City J", 490),
        ("City J", "City F", 570), ("City J", "City I", 490)
    ]
    [g1.add_edge(ori, des, cos) for ori, des, cos in e1]
    g1.show()
    g1.min_path("City B", "City H")


