import sys
from functools import partial
from operator import is_not
from typing import Literal

from astar import Graph, Node


def create_graph() -> Graph:
    graph = Graph()

    edges = {
        'A': [
            ('B', 0.4),
            ('C', 0.2)],
        'B': [
            ('D', 0.5),
            ('E', 1.0)],
        'C': [
            ('D', 2.2)],
        'D': [
            ('A', 0.1),
            ('E', 5.9)],
        'F': [
            (None, 0.0)],
    }

    keys = [ key for key in edges.keys() ]
    relations = [ key[0] for _, values in edges.items() for key in values ]

    nodes = list(set(keys) | set(relations))
    nodes = list(filter(partial(is_not, None), nodes))

    instances = {}
    for node in nodes:
        instances[node] = Node(node)

    for nodes in edges:
        for relation in edges[nodes]:
            graph.add(
                source=instances[nodes],
                destination=instances[relation[0]] if relation[0] != None else None,
                cost=relation[1],)

    return graph


def main(_: list[str]) -> Literal[0]:
    graph = create_graph()
    graph.print()

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
