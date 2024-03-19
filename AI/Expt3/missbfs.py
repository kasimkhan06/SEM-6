import queue as Queue

def storePath(initial, final, parent):
    allPaths = []
    for check in parent[final]:
        path = [final]
        curr = check
        while curr != initial:
            path.append(curr)
            # Accessing the parent of the current node, which is a tuple
            curr = parent[curr][-1]  # Take the last element of the tuple
        path.append(initial)
        path = path[::-1]
        allPaths.append(path)
    return allPaths

def generateSucc(currNode): ##to generate the successor nodes
    M , C , B = currNode ## curr Node detials
    if B == 'L' : ## boat is at the left side of the bank 
        return [(M - 1 , C , 'R') , (M , C-1 , 'R') , (M-2 , C , 'R') , (M , C-2 , 'R'), (M-1 , C-1 , 'R')]
    else : ## Boat is at the right side of the bank
        return [(M+1 , C , 'L') , (M , C+1 , 'L') , (M+2 , C , 'L')  , (M , C+2 , 'L') , (M+1 , C+1 , 'L')]
    
def isValid(currNode , totalMiss , totalCani):
    M , C , B = currNode ## curr Node details 
    ## check at the left side of the bank
    if M >= 0 and M <= totalMiss and C >= 0 and C <= totalCani :
        if(M > 0 and M < C):
            return False
    else :
        return False
    
    ## right side of the bank
    if (totalMiss - M >= 0 and totalMiss - M <= totalMiss and totalCani - C >=0 and totalCani - C <= totalCani) :
        if(totalMiss - M > 0 and totalMiss-M < totalCani - C):
            return False
    else :
        return False
    return True

def missCanibal(miss , cani , initial , final):
    #setting up the initial conditions
    allPaths = []
    q = Queue.Queue()
    vis = set()
    q.put(initial)
    vis.add(initial)
    parent = {} ## to store parents of the nodes to retrive the path
    while not q.empty() :
        currNode = q.get() #current node
        if currNode == final:
            continue
        #generate successors or child nodes of curr state
        succNodes = generateSucc(currNode)
        for childrenNode in succNodes:
            if childrenNode not in vis and isValid(childrenNode , miss , cani):
                q.put(childrenNode)
                if(childrenNode != final) :
                    vis.add(childrenNode)
                if childrenNode in parent :
                    parent[childrenNode] = parent[childrenNode] + (currNode,)
                else :
                    parent[childrenNode] = (currNode ,)
    allPaths = storePath(initial , final , parent)
    return allPaths

missionaries = 3
canibals = 3
initial = (3 , 3 ,'L')
final = (0 , 0 , 'R')
allPaths = missCanibal(missionaries , canibals , initial , final)
if not allPaths:
    print("No Solution")
else :
    print("The Solution is : ")
    for path in allPaths:
        print(path)