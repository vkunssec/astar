from astar import Graph, Node


g = Graph()

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')

g.addEdge(a, b, 0.4)
g.addEdge(a, c, 0.2)
g.addEdge(b, d, 0.5)
g.addEdge(b, e, 1.0)
g.addEdge(c, d, 2.2)
g.addEdge(d, a, 0.1)
g.addEdge(d, e, 5.9)


g.print()
