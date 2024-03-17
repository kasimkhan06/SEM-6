import copy
def findEmptySpot(currState):
    for i in range(len(currState)):
        for j in range(len(currState)):
            if currState[i][j] == 0 :
                return i , j
            
def computeCost(currState , finalState):
    cost = 0
    for i in range(len(currState)):
        for j in range(len(finalState)):
            if currState[i][j] != finalState[i][j] :
                cost+=1
    return cost

initial  = [[1,2,3],[5,6,0],[7,8,4]]
final = [[1,2,3],[5,8,6],[0,7,4]]

#start the algorithm
#generate all the children nodes and check which gives the best value to explore further 
currState = copy.deepcopy(initial) #initialize the algorithm

#To check up , right , down , left
drow = [-1 , 0 , +1 , 0] 
dcol = [0 , +1 , 0 , -1]

h_x = 0 + computeCost(currState , final)
level = 1

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
    found = False
    for index in range(len(drow)) :
        nrow = drow[index] + i
        ncol = dcol[index] + j
        #check if the new indices are valid
        if nrow >= 0 and nrow < len(currState) and ncol >= 0 and ncol < len(currState) :
            childrenNode[i][j] = currState[nrow][ncol]
            childrenNode[nrow][ncol] = 0
            #calculate the heuristic value 
            newCost = level + computeCost(childrenNode , final)
            if newCost <= h_x : #we found a better state
                found = True
                h_x = newCost
                optimalState =  copy.deepcopy(childrenNode)

            #reverse the changes
            childrenNode[nrow][ncol] = childrenNode[i][j]
            childrenNode[i][j] = 0

    if not found : #we didnt get a better state than current
        break

    currState = copy.deepcopy(optimalState)
    level += 1
