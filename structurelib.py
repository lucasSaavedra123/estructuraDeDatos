class Node:
    def __init__(self,text):
        self.text = text
    
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return self.text
    
class Edge:
    def __init__(self,sourceNode,destinationNode):
        self.sourceNode = sourceNode
        self.destinationNode = destinationNode

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.sourceNode) + " -> " + str(self.destinationNode)


class Graph:
    def __init__(self,nodes = None, edges = None):
        
        if nodes is None:
            self.nodes = set()
        else:
            self.nodes = set(nodes)
        
        if edges is None:
            self.edges = set()
        else:
            self.edges = set(edges)
    
    
    @classmethod
    def couldBeIsomorphic(cls,graphOne,graphTwo):
        
        if not (graphOne.hasSameEdgesCardinality(graphTwo) and graphOne.hasSameNodesCardinality(graphTwo)):
            return False
        elif sorted(graphOne.degreesMultiset()) == sorted(graphTwo.degreesMultiset()):
            return False
        elif len(graphOne.loops()) != len(graphTwo.loops()):
            return False

        return True
    
    def loops(self):
        loopsArray = []
        
        for edge in self.edges:
            if edge.destinationNode == edge.sourceNode:
                loopsArray.append(edge.sourceNode)
        
        return loopsArray 
    
    def inputGrade(self,aNode):
        return len(self.leftNeighbourhood(aNode))

    def outputGrade(self,aNode):
        return len(self.rightNeighbourhood(aNode))

    def grade(self,aNode):
        return (self.inputGrade(aNode),self.outputGrade(aNode)) 

    def degreesMultiset(self):
        degreesMultiset = []

        for node in self.nodes:
            degreesMultiset.append(self.grade(node))

        return degreesMultiset

    def hasSameEdgesCardinality(self,anotherGraph):
        return self.edgesCardinality() != anotherGraph.edgesCardinality()

    def hasSameNodesCardinality(self,anotherGraph):
        return self.nodesCardinality() != anotherGraph.nodesCardinality()

    def addNode(self,node):
        self.nodes.add(node)
    
    def addEdge(self,edge):
        self.edges.add(edge)
    
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        graphToTextString = "Nodes: \n"
        
        for node in self.nodes:
            graphToTextString += str(node) + "\n"
        
        graphToTextString += "Edges: \n"
        
        for edge in self.edges:
            graphToTextString += str(edge) + "\n"
                
        return graphToTextString
    
    def nodesCardinality(self):
        return len(self.nodes)
    
    def edgesCardinality(self):
        return len(self.edges)

    def toAdjacencyMatrix(self):
        matrix = {}
        
        for node in self.nodes:
            matrix[node] = {}

            for auxNode in self.nodes:
                matrix[node][auxNode] = 0
        
        for edge in self.edges:
            matrix[edge.sourceNode][edge.destinationNode] = 1
        

        return matrix
    
    def isSymmetric(self):
        matrix = self.toAdjacencyMatrix()
        
        for nodeOne in self.nodes:
            for nodeTwo in self.nodes:
                if matrix[nodeOne][nodeTwo] != matrix[nodeTwo][nodeOne] and nodeOne != nodeTwo:
                    return False
        
        return True
    
    def leftNeighbourhood(self, aNode):
        matrix = self.toAdjacencyMatrix()
        arrayOfNodes = []
        
        for node in self.nodes:
            if matrix[node][aNode] == 1:
                arrayOfNodes.append(node)
        
        return arrayOfNodes
    
    def rightNeighbourhood(self, aNode):
        matrix = self.toAdjacencyMatrix()
        arrayOfNodes = []
        
        for node in self.nodes:
            if matrix[aNode][node] == 1:
                arrayOfNodes.append(node)
        
        return arrayOfNodes
    
    def path(self,sourceNode,destinationNode):
    
        OPEN = []
        CLOSED = []
        OPEN.append((sourceNode,None))

        while len(OPEN) != 0:
            auxiliarSet = set()
            tupleFromOpen = OPEN.pop()
            CLOSED.append(tupleFromOpen)
            rightNeighbourhood = self.rightNeighbourhood(tupleFromOpen[0])

            if destinationNode in rightNeighbourhood:
                CLOSED.append((destinationNode,tupleFromOpen[0]))
                return CLOSED
            
            for element in OPEN:
                auxiliarSet.add(element[0])
            for element in CLOSED:
                auxiliarSet.add(element[1])
            
            for node in set(rightNeighbourhood) - auxiliarSet:
                OPEN.append((node,tupleFromOpen[0]))
