from astar import Edge, Node


class Graph:
    def __init__(self) -> None:
        self.graph = dict()

    def checkEdge(self, node: Node) -> None:
        if node not in self.graph:
            self.graph[node] = []

    def addEdge(self, source: Node, destination: Node, cost: float) -> None:
        self.checkEdge(source)
        self.checkEdge(destination)

        edge = Edge.create(destination, cost)
        self.graph[source].append(edge)

    def print(self) -> None:
        for source, destination in self.graph.items():
            print(f'{source} -> {destination}')
