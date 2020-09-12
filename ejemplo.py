from structurelib import *

nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")

aGraph = Graph([nodeA,nodeB,nodeC,nodeD,nodeE], [Edge(nodeA,nodeA), Edge(nodeC,nodeB), Edge(nodeB,nodeB), Edge(nodeB,nodeD), Edge(nodeC,nodeE), Edge(nodeC,nodeD), Edge(nodeD,nodeB),Edge(nodeA,nodeD)])

print(aGraph)
print(aGraph.loops())