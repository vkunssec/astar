from astar import Edge, Node


class Graph:
    def __init__(self) -> None:
        self.graph = dict()

    def __contains__(self, node: Node) -> bool:
        return node in self.graph

    def check(self, node: Node) -> None:
        for key in self.graph.keys():
            if str(key) == str(node.node):
                return
        if node not in self.graph:
            self.graph[node] = []

    def add(self, source: Node, destination: Node, cost: float) -> None:
        self.check(source)

        if destination != None:
            self.check(destination)

            edge = Edge.create(destination, cost)
            self.graph[source].append(edge)
        else:
            self.graph[source] = []

    def print(self) -> None:
        for source, destination in self.graph.items():
            print(f'{source} -> {destination}')
