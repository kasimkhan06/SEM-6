import queue as Queue
def storePath(initial , final , parent , allPaths) :
    for currNode in final:
        path = []
        curr = currNode
        if curr not in parent.keys():
            continue
        while curr != initial:
            path.append(curr)
            curr = parent[curr]
        path.append(initial)
        path = path[::-1]
        allPaths.add(tuple(path))
    return allPaths
def JugBFS(jug1Cap , jug2Cap , initial , final):
    #setting up the intial states
    q = Queue.Queue()
    allPaths = set()
    vis = set()
    parent = {}
    q.put(initial)
    while not q.empty():
        curr = q.get()
        if curr in final:
            storePath(initial , final , parent , allPaths)
            continue
        jug1 , jug2 = curr
        #filling and emptying jug1 and jug2
        succ = [(jug1Cap , jug2) , (jug1 , jug2Cap) , (0 , jug2) , (jug1 , 0)] 
        #transfer water from jug1 to jug2
        spaceRemJug2 = jug2Cap - jug2 
        #can we pour entire water in jug2 ??
        ## yes if the space remaining in jug 2 >= what is in jug1
        if spaceRemJug2 >= jug1 :
            succ.append((0 , jug2 + jug1))
        else :
            succ.append((jug1 - spaceRemJug2 , jug2Cap))
        
        ## transfer water from jug2 to jug1
        spaceRemJug1 = jug1Cap - jug1
        if spaceRemJug1 >= jug2 :
            succ.append((jug1 + jug2 , 0))
        else :
            succ.append((jug1Cap , jug2 - spaceRemJug1))

        ##dfs calls for all of these child nodes or succ states
        for s in succ:
            if s not in vis:
                vis.add(s)
                q.put(s)
                parent[s] = curr
    return allPaths

allPaths = JugBFS(3 , 4 , (0,0) , [(0,2),(1,2),(2,2),(3,2)])
if not allPaths :
    print("No Solution")
else :
    print("Solution is : ")
    for path in allPaths:
        print(path)