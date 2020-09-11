from structurelib import *

nodeA = Node("Silla")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("Tornillo")

aGraph = Graph([nodeA,nodeB,nodeC,nodeD,nodeE], [Edge(nodeB,nodeC), Edge(nodeC,nodeB), Edge(nodeB,nodeA), Edge(nodeB,nodeD), Edge(nodeC,nodeE), Edge(nodeC,nodeD), Edge(nodeD,nodeB),Edge(nodeA,nodeD)])

print(aGraph)
print(aGraph.path(nodeA,nodeB))