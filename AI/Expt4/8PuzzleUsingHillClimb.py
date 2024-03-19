import copy
import numpy as np

def findEmptySpot(currState):
    for i in range(len(currState)):
        for j in range(len(currState)):
            if currState[i][j] == 0 :
                return i , j
            
def findlocationinCurr(ele , currState):
    for i in range(len(currState)):
        for j in range(len(currState)):
            if currState[i][j] == ele :
                return i , j

def findlocationinFinal(ele , finalState) :
    for i in range(len(finalState)):
        for j in range(len(finalState)):
            if finalState[i][j] == ele :
                return i , j

def computeCost(currState , finalState):
    cost = 0
    for i in range(len(currState)):
        for j in range(len(finalState)):
            x1 , y1 = findlocationinCurr(currState[i][j] , currState)
            x2 , y2 = findlocationinFinal(currState[i][j] , finalState)
            cost += abs(x2-x1) + abs(y2-y1)
    return cost

def _8PuzzleUsingHillClimb(initial , final):
    #start the algorithm
    #generate all the children nodes and check which gives the best value to explore further 
    currState = copy.deepcopy(initial) #initialize the algorithm

    #To check up , right , down , left
    drow = [-1 , 0 , +1 , 0] 
    dcol = [0 , +1 , 0 , -1]

    h_x = computeCost(currState , final)

    while True : 

        #print the final selected Node
        for i in range(len(currState)):
            for j in range(len(currState)):
                print(currState[i][j] , " " ,end="")
            print()
        print()

        #generate the children Nodes
        #find the empty spot
        if currState == final :
            break
        i , j = findEmptySpot(currState)
        #move the surrounding four to current four states
        childrenNode = copy.deepcopy(currState)
        optimalState = copy.deepcopy(currState) #to store the best state among the chidren
        for index in range(len(drow)) :
            nrow = drow[index] + i
            ncol = dcol[index] + j
            #check if the new indices are valid
            if nrow >= 0 and nrow < len(currState) and ncol >= 0 and ncol < len(currState) :
                childrenNode[i][j] = currState[nrow][ncol]
                childrenNode[nrow][ncol] = 0
                #calculate the heuristic value 
                newCost = computeCost(childrenNode , final)
                if newCost < h_x : #we found a better state
                    h_x = newCost
                    optimalState =  copy.deepcopy(childrenNode)

                #reverse the changes
                childrenNode[nrow][ncol] = childrenNode[i][j]
                childrenNode[i][j] = 0

        if currState == optimalState : #we didnt find any optimal state
            break

        currState = copy.deepcopy(optimalState)

initial  = [[1,2,0],[5,6,3],[7,8,4]]
final = [[1,2,3],[5,8,6],[0,7,4]]
_8PuzzleUsingHillClimb(initial , final)