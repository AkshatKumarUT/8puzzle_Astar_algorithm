'''
A* Algorithm
Evaluation Function = Path Cost from root + Path Cost to Goal
Use Manhattan distance to calculate Path Cost from Goal

Use DFS to

First construct the 8 panels

'''

class Node:
    def __init__(self, state, depth, parent=None):
        self.state = state
        self.depth = depth + 1
        self.f = self.evaluationFunction(self.state, self.depth)
        self.parent = parent
        self.moveDirection = None

    #f = h + g, h = distance from goal, g = distance from start
    def evaluationFunction(self, state, depth):
        h = self.manhattanDistance(state)
        g = depth
        f = g + h
        return f
    
    def setMoveDirection(self, direction):
        self.moveDirection = direction

    #calculates function h(n) by calculating the manhattan distance from n to goal
    def manhattanDistance(self, square):
        totalDistance = 0
        #print("manhattan distance:")
        for i in range(len(square)):
            for j in range(len(square[i])): 
                #Uses modulus and integer division to find the optimal pos given value
                if (square[i][j] == 0):
                    optimalPos = (2, 2)
                else:
                    optimalPos = (((square[i][j]-1)//3), (square[i][j]-1)%3)
                #calculatees distance from actual pos to optimal pos
                distance = abs(optimalPos[0] - i) + abs(optimalPos[1] - j)
                #print("distance for " + str(square[i][j]) + " is " + str(distance) + " (" + str(optimalPos[0]) + " + " + str(abs(optimalPos[1] - j)) + ")")
                totalDistance += distance
        #print("total distance is " + str(totalDistance))
        return totalDistance
    
    #generates all possible states that could be made after 
    def generateNodes(self):
        moves, zeroPos = self.possibleMoves(self.moveDirection)
        if("Right" in moves):
            rightState = self.cloneList(self.state)
            rightState = self.swapTiles(rightState, zeroPos, (zeroPos[0], zeroPos[1]+1))
            if not self.checkVisited(rightState):
                rightNode = Node(rightState, self.depth, self)
                rightNode.setMoveDirection("Right")
                self.addToLeavesList(rightNode)
        
        if("Up" in moves):
            upState = self.cloneList(self.state)
            upState = self.swapTiles(upState, zeroPos, (zeroPos[0]-1, zeroPos[1]))
            if not self.checkVisited(upState):
                upNode = Node(upState, self.depth, self)
                upNode.setMoveDirection("Up")
                self.addToLeavesList(upNode)
                
        if("Down" in moves):
            downState = self.cloneList(self.state)
            downState = self.swapTiles(downState, zeroPos, (zeroPos[0]+1, zeroPos[1]))
            if not self.checkVisited(downState):
                downNode = Node(downState, self.depth, self)
                downNode.setMoveDirection("Down")
                #print("node created")
                #printSquare(downState)
                self.addToLeavesList(downNode)
                
        if("Left" in moves):
            leftState = self.cloneList(self.state)
            leftState = self.swapTiles(leftState, zeroPos, (zeroPos[0], zeroPos[1]-1))
            if not self.checkVisited(leftState):
                leftNode = Node(leftState, self.depth, self)
                leftNode.setMoveDirection("Left")
                #print("node created")
                #printSquare(leftState)
                self.addToLeavesList(leftNode)
                
        
    #adds states to candidatees list sorted by least cost to most cost
    def addToLeavesList(self, node):
        if len(candidatesList) == 0:
            candidatesList.append(node)
        else:
            for i in range (len(candidatesList)):
                if(node.f <= candidatesList[i].f):
                    candidatesList.insert(i, node)
                    break
            else:
                candidatesList.append(node)
            
    #finds where zero is
    def findZero(self, square):
        for i in range(len(square)):
            for j in range(len(square[i])):
                if square[i][j] == 0:
                    return (i, j)

    #finds the possible moves that that the zero can make
    def possibleMoves(self, lastMove):
        zeroPos = self.findZero(self.state)
        moves = ["Up", "Down", "Left", "Right"]
        #if zero is on the top row
        if(zeroPos[0] == 0 or lastMove == "Down"):
            #remove up
            moves.remove("Up")
        #if zero is on the bottom row
        if(zeroPos[0] == len(square)-1 or lastMove == "Up"):
            #remove down
            moves.remove("Down")
        #if zero is on left
        if(zeroPos[1] == 0 or lastMove == "Right"):
            #remove left
            moves.remove("Left")
        #if zero is on right
        if(zeroPos[1] == len(square[0])-1 or lastMove == "Left"):
            #remove right
            moves.remove("Right")

        return moves, zeroPos

    #swaps the zero 
    def swapTiles(self, state, posOne, posTwo):
        #print(str(posOne[0]) + " " + str(posOne[1]))
        #print(str(posTwo[0]) + " " + str(posTwo[1]))
        temp = state[posOne[0]][posOne[1]]
        state[posOne[0]][posOne[1]] = state[posTwo[0]][posTwo[1]]
        state[posTwo[0]][posTwo[1]] = temp
        return state

    #clone lists because lists are pass by reference
    def cloneList(self, array):
        newArray = [None] * len(array)
        for i in range(len(array)):
            newArray[i] = array[i].copy()
        return newArray
    
    #check if state has been visited before
    def checkVisited(self, state):
        for i in range(len(visitedList)):
            if state == visitedList[i].state:
                return i
        return False

    #function that prints the current state
    def printState(self):
        for i in range(len(self.state)):
            j = 0
            print (str(self.state[i][j]) + " " + str(self.state[i][j+1]) + " " + str(self.state[i][j+2]))
            

#function that prints the current state
def printSquare(square):
    for i in range(len(square)):
        j = 0
        print (str(square[i][j]) + " " + str(square[i][j+1]) + " " + str(square[i][j+2]))
    

square = [[8, 3, 2], [4, 7, 1], [0, 5, 6]]

goalState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
visitedList = []
candidatesList = []

printSquare(square)
print("")

rootNode = Node(square, 0)
visitedList.append(rootNode)

currentNode = rootNode
goalFound = False


while not goalFound:
#for i in range(9):
    if(currentNode.state == goalState):
        goalFound = True
        print("goalState found")
        break
    
    currentNode.generateNodes()
    
    bestNode = candidatesList.pop(0)
    bestDirection = bestNode.moveDirection
        
    #printSquare(bestNode.state)
    #print(bestDirection)
    
    #print("")
        
    visitedList.append(bestNode)
    
    currentNode = bestNode

path = []
numberOfMoves = 0

def getPath(node, numberOfMoves):
    path.append(node.moveDirection)
    if node.parent is not None:
        numberOfMoves = numberOfMoves + 1
        return getPath(node.parent, numberOfMoves)
    else:
        return numberOfMoves
    
number = getPath(currentNode, numberOfMoves)
print("number of moves is " + str(number))

print("path is: ")
for i in range(len(path)):
    print(path[len(path) - 1 - i])
