class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, flight):
        origin = flight[0]
        destination = flight[1]
        price = flight[2]
        connection_time = flight[3]
        if origin not in self.adjacency_list:
            self.adjacency_list[origin] = []
        if destination not in self.adjacency_list:
            self.adjacency_list[destination] = []
        self.adjacency_list[origin].append((destination, price, connection_time))

    def dijkstra(self, origin, destination, waiting_limit):
        unvisited = list(self.adjacency_list.keys())
        weights = {vertex: (float("inf"), 0, waiting_limit) for vertex in self.adjacency_list}
        weights[origin] = (0, 0, waiting_limit) 
        predecessors = {}
        while unvisited:
            current = min(unvisited, key=lambda vertex: weights[vertex][0])
            if weights[current][0] == float("inf"):
                break
            for neighbor in self.adjacency_list[current]:
                nvertex, nprice, nconnection_time = neighbor[0], neighbor[1], neighbor[2]
                path_price = weights[current][0] + nprice
                path_connection_time = weights[current][1] 
                if neighbor != destination:
                    path_connection_time += nconnection_time
                    path_price += 30
                if path_price < weights[nvertex][0] and path_connection_time <= waiting_limit:
                        weights[nvertex] = (path_price, path_connection_time, waiting_limit)
                        predecessors[nvertex] = current
            unvisited.remove(current)
        path = []
        current = destination
        while current in predecessors.keys():
            path.insert(0, (current, weights[current]))
            current = predecessors[current]
        path.insert(0, (origin, weights[origin]))
        return path

    def show_graph(self):
        print("Graph")
        for origin in self.adjacency_list:
            print(origin, [destination for destination in self.adjacency_list[origin]])

    def show_path(self, origin, destination, waiting_limit=float('inf')):
        path = self.dijkstra(origin, destination, waiting_limit)
        price = f"Price: ${path[-1][1][0]}"
        connection_time = path[-1][1][1]
        airports = len(path)
        if airports <= 1:
            print("Path not found")
            return
        
        scale = "Direct Flight"
        if airports > 2:
            if connection_time != 0: 
                scale = f"Connecting flight - Waiting time: {connection_time}min"
            else:
                scale = f"Same-plane with stopover - Stopovers: {airports-2}"

        print(f"Best path from {origin} to {destination}")
        for i in range(airports):
            if i != airports-1:
                print(f'{path[i][0]}', end = " -> ")
            else:
                print(f'{path[i][0]}')
        print(scale)
        print(price)
                    
if __name__ == "__main__":
    flights = [
        #(origin, destination, price, connection_time)
        ("GRU", "GIG", 300, 0),
        ("GRU", "CNF", 200, 0),
        ("CNF", "GIG", 150, 0),
        ("GRU", "POA", 250, 0),
        ("POA", "GIG", 320, 60),

        ("GRU", "SSA", 500, 0),
        ("GRU", "BSB", 400, 0),
        ("BSB", "SSA", 300, 0),
        ("GRU", "GIG", 300, 0),
        ("GIG", "SSA", 350, 90),

        ("GRU", "MIA", 1200, 0),
        ("GRU", "PTY", 1000, 0),
        ("PTY", "MIA", 500, 120),
        ("GRU", "LIM", 900, 0),
        ("LIM", "MIA", 700, 75),

        ("BSB", "MIA", 1300, 0),
        ("GRU", "POA", 250, 0),
        ("GRU", "REC", 600, 0),
        ("BSB", "REC", 400, 0),
        ("BSB", "MVD", 800, 0),
        ("POA", "MVD", 300, 180),
    ]
    graph = Graph()
    [graph.add_edge(flight) for flight in flights]
    # graph.show_graph()
    graph.show_path("GRU", "MVD", 60)








