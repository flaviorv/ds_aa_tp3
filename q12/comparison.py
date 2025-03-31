from random import randrange
from time import time

class Graph:
    def __init__(self, length, variation):
        self.vertices = length
        self.adjacency_matrix = [[randrange(1, variation) if i != j else 0 for i in range(length)] for j in range(length)]

    def show(self):
        if self.vertices <= 20:
            for vertex in self.adjacency_matrix:
                print(vertex)
        else:
            print(f"Matrix length is {self.vertices}")

    def dijkstra(self, origin, destination):
        unvisited = [i for i in range(self.vertices)]
        weights = [float("inf") for i in range(self.vertices)]
        weights[origin] = 0
        while unvisited:
            current = min(unvisited, key=lambda vertex: weights[vertex])
            if weights[current] == float("inf"):
                break
            if current == destination:
                return weights[destination]
            for neighbor in range(self.vertices):
                if current != neighbor:
                    weight = self.adjacency_matrix[current][neighbor]
                    new_weight = weights[current] + weight
                    if new_weight < weights[neighbor]:
                        weights[neighbor] = new_weight
            unvisited.remove(current)
        return 0

    def dijkstra_for_all(self):
        copy = [[self.adjacency_matrix[i][j] for j in range(self.vertices)] for i in range(self.vertices)]
        for ori in range(self.vertices):
            for dest in range(self.vertices):
                min_weight = self.dijkstra(ori, dest)
                copy[ori][dest] = min_weight
        return copy
    
    def floyd_warshall(self):
        copy = [[self.adjacency_matrix[i][j] for j in range(self.vertices)] for i in range(self.vertices)]
        for k in range(self.vertices):
            for i in range(self.vertices):
                for j in range(self.vertices):
                    if copy[i][k] + copy[k][j] < copy[i][j]:
                        copy[i][j] = copy[i][k] + copy[k][j]
        return copy

    def show_result(self, graph):
        if self.vertices <= 20:
            for vertex in graph:
                print(vertex)
        else:
            print(f"Matrix length is {self.vertices}")
    
    def comparison(self):
        print("\nGraph")
        self.show()
        
        start1 = time()
        dijkstra = self.dijkstra_for_all()
        time1 = round(time() - start1, 3)

        start2 = time()
        floyd = self.floyd_warshall()
        time2 = round(time() - start2, 3)

        print("\nDijkstra")
        self.show_result(dijkstra)
        print(f"Time:", time1, "seconds")
        
        print("\nFloyd Warshall")
        self.show_result(floyd)
        print(f"Time:", time2, "seconds")

if __name__ == "__main__":
    g1 = Graph(10, 10)
    g1.comparison()

    g2 = Graph(10, 1000)
    g2.comparison()

    g3 = Graph (100, 10)
    g3.comparison()

    g4= Graph(100, 1000)
    g4.comparison()
        
        
    