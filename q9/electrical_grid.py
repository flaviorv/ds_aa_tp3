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
    cities = [
        ("City A", "City B", 12),
        ("City A", "City C", 15),
        ("City B", "City D", 18),
        ("City B", "City E", 8),
        ("City C", "City D", 10),
        ("City C", "City F", 25),
        ("City D", "City G", 14),
        ("City E", "City H", 11),
        ("City E", "City I", 16),
        ("City F", "City G", 7),
        ("City F", "City J", 20),
        ("City G", "City H", 13),
        ("City H", "City I", 9),
        ("City I", "City J", 10)
    ]
    [graph.add_edge(ori, des, cost) for ori, des, cost in cities]
    # graph.show()
    print("Obtaining the minimum cost to expand the electrical grid through the Prim's MST")
    graph.prim("City E")