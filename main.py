import sys
from typing import Literal

from astar import Graph, Node


def main(_: list[str]) -> Literal[0]:
    g = Graph()

    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    f = Node('F')

    g.add(a, b, 0.4)
    g.add(a, c, 0.2)
    g.add(b, d, 0.5)
    g.add(b, e, 1.0)
    g.add(c, d, 2.2)
    g.add(d, a, 0.1)
    g.add(d, e, 5.9)
    g.add(f, None, 0)

    g.print()

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
