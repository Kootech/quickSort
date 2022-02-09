


x = [
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1],
    ]

xlen = len(x)
def removeIsland(x):
    
    i = 0
    j = 0
    for i in range(len(x)):
        for j in range(len(x[i])):
            number = x[i][j]
            if number == 1:
                if number is isIsland(i, j):
                    x.replace('1', '0')


def isIsland(i, j):
    if x[i][j] is not isEdge(i, j):
        num =1
        if num==x[i-1][j]:
            if x[i-1][j] is isEdge(i-1, j):
                return False
        elif num==x[i][j+1]:
            if x[i][j+1] is isEdge(i, j+1):
                return False
        elif num==x[i+1][j]:
            if x[i+1][j] is isEdge(i+1, j):
                return False
        elif num==x[i][j-1]:
            if x[i][j-1] is isEdge(i, j-1):
                return False
        else:
            return True

    else:
        return True 
            


def isEdge(i, j):
    if i==0 or j==0 or i==xlen or j==xlen:
        return True

removeIsland(x)
