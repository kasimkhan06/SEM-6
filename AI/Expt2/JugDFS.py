def JugDFS(jug1Cap , jug2Cap , initial , final):
    visited = set()
    allPaths = []
    path = [(initial)]
    def __dfs(curr):
        if curr in final:
            allPaths.append(path.copy())
            return
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
            if s not in visited:
                path.append(s)
                visited.add(s)
                __dfs(s)
                path.pop() ##backtracking
                # visited.remove(s)
    visited.add(initial)
    __dfs(initial)
    return allPaths

allPaths = JugDFS(3 , 4 , (0,0) , [(0,2) , (2,0)])
if not allPaths :
    print("No Solution")
else :
    print("Solution is : ")
    for path in allPaths:
        print(path)