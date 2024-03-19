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

def missCanibal(missionaries , canibals , initial , final):
    vis = set()
    allPaths = []
    path = [(initial)]
    def __dfs(currNode):
        if currNode == final:
            allPaths.append(path.copy())
            return
        succNodes = generateSucc(currNode)
        for childrenNode in succNodes:
            if childrenNode not in vis and isValid(childrenNode , missionaries , canibals):
                path.append(childrenNode)
                if childrenNode != final :
                    vis.add(childrenNode)
                __dfs(childrenNode)
                path.pop()
    vis.add(initial)
    __dfs(initial)
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