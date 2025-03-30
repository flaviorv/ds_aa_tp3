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
        ("Neighborhood A", "Neighborhood B", 2),
        ("Neighborhood A", "Neighborhood C", 3),
        ("Neighborhood B", "Neighborhood D", 4),
        ("Neighborhood B", "Neighborhood E", 1),
        ("Neighborhood C", "Neighborhood D", 2),
        ("Neighborhood C", "Neighborhood F", 5),
        ("Neighborhood D", "Neighborhood G", 3),
        ("Neighborhood E", "Neighborhood H", 2),
        ("Neighborhood E", "Neighborhood I", 4),
        ("Neighborhood F", "Neighborhood G", 1),
        ("Neighborhood F", "Neighborhood J", 3),
        ("Neighborhood G", "Neighborhood H", 2),
        ("Neighborhood H", "Neighborhood I", 3),
        ("Neighborhood I", "Neighborhood J", 2)
    ]
    [graph.add_edge(ori, des, cost) for ori, des, cost in neighborhoods]
    # graph.show()
    print("Obtaining the minimum cost to bring fiber optics to all neighborhoods on the graph")
    graph.prim("Neighborhood C")