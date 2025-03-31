class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 not in self.adjacency_list:
            self.adjacency_list[vertex1] = []
        if vertex2 not in self.adjacency_list:
            self.adjacency_list[vertex2] = []
        self.adjacency_list[vertex1].append((vertex2, weight))
        self.adjacency_list[vertex2].append((vertex1, weight))

    def show(self):
        for vertex in self.adjacency_list:
            print(vertex, self.adjacency_list[vertex])

    def prim(self, origin):
            vertices = {}
            total_weight = 0
            for vertex in self.adjacency_list:
                vertices[vertex] = {}
                vertices[vertex]["selected"] = False
                vertices[vertex]["weight"] = float('inf')
                vertices[vertex]["parent"] = None
            vertices[origin]["weight"] = 0  
            for _ in range(len(self.adjacency_list)):
                minimum = float('inf')
                _selected = -1
                for vertex in self.adjacency_list:
                    if not vertices[vertex]["selected"] and vertices[vertex]["weight"] < minimum:
                        minimum = vertices[vertex]["weight"]
                        _selected = vertex
                total_weight += minimum
                vertices[_selected]["selected"] = True
                for vertex, weight in self.adjacency_list[_selected]:
                    if 0 < weight < vertices[vertex]["weight"] and not vertices[vertex]["selected"]:
                        vertices[vertex]["weight"] = weight
                        vertices[vertex]["parent"] = _selected
            for key in vertices:
                if key != origin:
                    print(f"{vertices[key]["parent"]} - {key}   {vertices[key]["weight"]} km")
            print(f"Network length: {total_weight} km")

if __name__ == "__main__":
    graph = Graph()
    regions = [
        ("Region 1", "Region 2", 9),
        ("Region 1", "Region 5", 4),
        ("Region 2", "Region 6", 3),
        ("Region 2", "Region 4", 7),
        ("Region 3", "Region 7", 8),
        ("Region 3", "Region 5", 6),
        ("Region 4", "Region 8", 2),
        ("Region 4", "Region 1", 5),
        ("Region 5", "Region 3", 10),
        ("Region 6", "Region 8", 6),
        ("Region 7", "Region 9", 4),
        ("Region 7", "Region 4", 3),
        ("Region 8", "Region 2", 5),
        ("Region 9", "Region 6", 7)
    ]
    [graph.add_edge(ori, des, cost) for ori, des, cost in regions]
    # graph.show()
    print("Obtaining the minimum path to reach each region and install a telephone network")
    graph.prim("Region 1")