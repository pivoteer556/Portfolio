#Artificial Intelligence Homework Assignment 1
#Program by Alex Wilkening
#This program finds the best solution to a "gem switcher" problem.

#To-Do list: find a way to make sure that the nodes actually go to the right parent


def main(StartingNodes):
    CurrentLayer = [] #A list of all nodes in our current layer
    if type(StartingNodes) is not Node:
        CurrentLayer = StartingNodes
    else:
        CurrentLayer.append(StartingNodes) #Add starting node to current layer
    AllNodesExpanded = [] #A list of every node we've expanded thusfar
    NextLayer = [] #A holder for the next layer of children
    currentIndex = 0 #instantiate loop variables
    Children = []
    #print(CurrentLayer)
    for myNode in CurrentLayer:
        #print(myNode)
        currentIndex += 1 #increment
        isSolution = checkNode(myNode) #check if this is our answer
        if isSolution == True: #check if this node is a solution
            Solution = getPath(myNode) #return the path we took
            return Solution #Here's our answer
        Children = generateChildren(myNode) #create children
        for Nodes in Children: #make those children the next layer
            NextLayer.append(Nodes)
    main(NextLayer) #pass in the next layer

def checkNode(myNode):
    if myNode.getData() == "DDDDDDDDD" or myNode.getData() == "EEEEEEEEE" or myNode.getData() == "RRRRRRRRR":
        print("found it")
        return True
    else:
        return False

def getPath(myNode):
    Solution = []
    Solution.append(myNode.getData())
    while myNode.hasParent() == True:
       Solution.append(myNode.getData()) 
       myNode = myNode.getParent()
       print(Solution)
    else:
        return Solution

def generateChildren(myNode):
    currentBoard = myNode.getData()
    Data1 = genNode1(currentBoard)#geneate the new boards (ugh)
    Data2 = genNode2(currentBoard)
    Data3 = genNode3(currentBoard)
    Data4 = genNode4(currentBoard)
    Data5 = genNode5(currentBoard)
    Data6 = genNode6(currentBoard)
    Data7 = genNode7(currentBoard)
    Data8 = genNode8(currentBoard)
    Data9 = genNode9(currentBoard)
    Node1 = Node(Data1)#generate the new nodes using the strings generated before
    Node2 = Node(Data2)
    Node3 = Node(Data3)
    Node4 = Node(Data4)
    Node5 = Node(Data5)
    Node6 = Node(Data6)
    Node7 = Node(Data7)
    Node8 = Node(Data8)
    Node9 = Node(Data9)
    Node1.setParent(myNode)#Set passed in node to parent
    Node2.setParent(myNode)
    Node3.setParent(myNode)
    Node4.setParent(myNode)
    Node5.setParent(myNode)
    Node6.setParent(myNode)
    Node7.setParent(myNode)
    Node8.setParent(myNode)
    Node9.setParent(myNode)
    Children = [Node1, Node2, Node3, Node4, Node5, Node6, Node7, Node8, Node9]
    return Children

def genNode1(myString):
    myString = list(myString)
    if myString[0] == "E":
        myString[0] = "D"
    if myString[1] == "E":
        myString[1] = "D"
    if myString[3] == "E":
        myString[3] = "D"
    if myString[0] == "D":
        myString[0] = "R"
    if myString[1] == "D":
        myString[1] = "R"
    if myString[3] == "D":
        myString[3] = "R"
    if myString[0] == "R":
        myString[0] = "E"
    if myString[1] == "R":
        myString[1] = "E"
    if myString[3] == "R":
        myString[3] = "E"
    myString = "".join(myString)
    return myString

def genNode2(myString):
    myString = list(myString)
    if myString[0] == "E":
        myString[0] = "D"
    if myString[1] == "E":
        myString[1] = "D"
    if myString[2] == "E":
        myString[2] = "D"
    if myString[4] == "E":
        myString[4] = "D"
    if myString[0] == "D":
        myString[0] = "R"
    if myString[1] == "D":
        myString[1] = "R"
    if myString[2] == "D":
        myString[2] = "R"
    if myString[4] == "D":
        myString[4] = "R"
    if myString[0] == "R":
        myString[0] = "E"
    if myString[1] == "R":
        myString[1] = "E"
    if myString[2] == "R":
        myString[2] = "E"
    if myString[4] == "R":
        myString[4] = "E"
    myString = "".join(myString)
    return myString

def genNode3(myString):
    myString = list(myString)
    if myString[1] == "E":
        myString[1] = "D"
    if myString[2] == "E":
        myString[2] = "D"
    if myString[5] == "E":
        myString[5] = "D"
    if myString[2] == "D":
        myString[2] = "R"
    if myString[1] == "D":
        myString[1] = "R"
    if myString[5] == "D":
        myString[5] = "R"
    if myString[0] == "R":
        myString[0] = "E"
    if myString[2] == "R":
        myString[2] = "E"
    if myString[5] == "R":
        myString[5] = "E"
    myString = "".join(myString)
    return myString

def genNode4(myString):
    myString = list(myString)
    if myString[0] == "E":
        myString[0] = "D"
    if myString[3] == "E":
        myString[3] = "D"
    if myString[4] == "E":
        myString[4] = "D"
    if myString[6] == "E":
        myString[6] = "D"
    if myString[0] == "D":
        myString[0] = "R"
    if myString[3] == "D":
        myString[3] = "R"
    if myString[4] == "D":
        myString[4] = "R"
    if myString[6] == "D":
        myString[6] = "R"
    if myString[0] == "R":
        myString[0] = "E"
    if myString[3] == "R":
        myString[3] = "E"
    if myString[4] == "R":
        myString[4] = "E"
    if myString[6] == "R":
        myString[6] = "E"
    myString = "".join(myString)
    return myString

def genNode5(myString):
    myString = list(myString)
    if myString[1] == "E":
        myString[1] = "D"
    if myString[3] == "E":
        myString[3] = "D"
    if myString[4] == "E":
        myString[4] = "D"
    if myString[5] == "E":
        myString[5] = "D"
    if myString[8] == "E":
        myString[8] = "D"   
    if myString[1] == "D":
        myString[1] = "R"
    if myString[3] == "D":
        myString[3] = "R"
    if myString[4] == "D":
        myString[4] = "R"
    if myString[5] == "D":
        myString[5] = "R"
    if myString[8] == "D":
        myString[8] = "R"
    if myString[1] == "R":
        myString[1] = "E"
    if myString[3] == "R":
        myString[3] = "E"
    if myString[4] == "R":
        myString[4] = "E"
    if myString[5] == "R":
        myString[5] = "E"
    if myString[8] == "R":
        myString[8] = "E"        
    myString = "".join(myString)
    return myString

def genNode6(myString):
    myString = list(myString)
    if myString[2] == "E":
        myString[2] = "D"
    if myString[5] == "E":
        myString[5] = "D"
    if myString[4] == "E":
        myString[4] = "D"
    if myString[8] == "E":
        myString[8] = "D"
    if myString[2] == "D":
        myString[2] = "R"
    if myString[4] == "D":
        myString[4] = "R"
    if myString[5] == "D":
        myString[5] = "R"
    if myString[8] == "D":
        myString[8] = "R"
    if myString[2] == "R":
        myString[2] = "E"
    if myString[4] == "R":
        myString[4] = "E"
    if myString[5] == "R":
        myString[5] = "E"
    if myString[8] == "R":
        myString[8] = "E"
    myString = "".join(myString)
    return myString

def genNode7(myString):
    myString = list(myString)
    if myString[3] == "E":
        myString[3] = "D"
    if myString[6] == "E":
        myString[6] = "D"
    if myString[7] == "E":
        myString[7] = "D"
    if myString[3] == "D":
        myString[3] = "R"
    if myString[6] == "D":
        myString[6] = "R"
    if myString[7] == "D":
        myString[7] = "R"
    if myString[3] == "R":
        myString[3] = "E"
    if myString[6] == "R":
        myString[6] = "E"
    if myString[7] == "R":
        myString[7] = "E"
    myString = "".join(myString)
    return myString

def genNode8(myString):
    myString = list(myString)
    if myString[4] == "E":
        myString[4] = "D"
    if myString[6] == "E":
        myString[6] = "D"
    if myString[7] == "E":
        myString[7] = "D"
    if myString[8] == "E":
        myString[8] = "D"
    if myString[4] == "D":
        myString[4] = "R"
    if myString[6] == "D":
        myString[6] = "R"
    if myString[7] == "D":
        myString[7] = "R"
    if myString[8] == "D":
        myString[8] = "R"
    if myString[4] == "R":
        myString[4] = "E"
    if myString[6] == "R":
        myString[6] = "E"
    if myString[7] == "R":
        myString[7] = "E"
    if myString[8] == "R":
        myString[8] = "E"
    myString = "".join(myString)
    return myString

def genNode9(myString):
    myString = list(myString)
    if myString[5] == "E":
        myString[5] = "D"
    if myString[7] == "E":
        myString[7] = "D"
    if myString[8] == "E":
        myString[8] = "D"
    if myString[5] == "D":
        myString[5] = "R"
    if myString[7] == "D":
        myString[7] = "R"
    if myString[8] == "D":
        myString[8] = "R"
    if myString[5] == "R":
        myString[5] = "E"
    if myString[7] == "R":
        myString[7] = "E"
    if myString[8] == "R":
        myString[8] = "E"
    myString = "".join(myString)
    return myString

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.Parent = None

    def getData(self):
        return self.data

    def getParent(self):
        return self.Parent

    def setData(self,newdata):
        self.data = newdata

    def setParent(self,newParent):
        self.Parent = newParent

    def hasParent(self):
        if self.Parent != None:
            return True
        else:
            return False

GetStartingNode = str(input("Please enter a string of 9 E's D's and R's to begin "))
while (len(GetStartingNode) != 9):
    GetStartingNode = str(input("Please enter a string of 9 E's D's and R's to begin "))
StartingNode = Node(GetStartingNode)
Solution = main(StartingNode)
print(Solution)


