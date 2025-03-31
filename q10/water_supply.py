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
                    print(f"{vertices[key]["parent"]} - {key}   ${vertices[key]["weight"]} million")
            print(f"Total cost: ${total_weight} million")

if __name__ == "__main__":
    graph = Graph()
    neighborhoods = [
        ("Neighborhood A", "Neighborhood B", 6),
        ("Neighborhood A", "Neighborhood F", 4),
        ("Neighborhood B", "Neighborhood E", 7),
        ("Neighborhood B", "Neighborhood C", 8),
        ("Neighborhood C", "Neighborhood H", 3),
        ("Neighborhood C", "Neighborhood G", 5),
        ("Neighborhood D", "Neighborhood J", 2),
        ("Neighborhood D", "Neighborhood I", 6),
        ("Neighborhood E", "Neighborhood G", 9),
        ("Neighborhood F", "Neighborhood I", 4),
        ("Neighborhood F", "Neighborhood H", 7),
        ("Neighborhood G", "Neighborhood J", 5),
        ("Neighborhood H", "Neighborhood A", 3),
        ("Neighborhood I", "Neighborhood B", 6)
    ]
    [graph.add_edge(ori, des, cost) for ori, des, cost in neighborhoods]
    # graph.show()
    print("Obtaining the minimum cost to install the water supply in the city")
    graph.prim("Neighborhood C")