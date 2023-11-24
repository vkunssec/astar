class Node:
    def __init__(self, attribute: str) -> None:
        self._node: str = attribute

    @property
    def node(self) -> str:
        return self._node

    @node.setter
    def node(self, attribute: str) -> None:
        self._node = attribute

    def __repr__(self) -> str:
        return self._node
