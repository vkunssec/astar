from .Node import Node


class Edge:
    def __init__(self) -> None:
        self.edge: float = 0

    @staticmethod
    def create(destination: Node, cost: float) -> tuple:
        return (str(destination), cost, )
