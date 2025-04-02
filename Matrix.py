def spiral(m,n):
    matrix=[[0]*n for _ in range(m)]
    srow,scol=0,0
    erow, ecol=m-1, n-1
    num=1

    while srow<=erow and scol<=ecol:
        # from top left to top right
        for i in range(scol,ecol+1):
            matrix[srow][i]=num
            num=num+1
        srow=srow+1

        #from top right to bottom right

        for i in range(srow,ecol+1):
            matrix[i][ecol]=num
            num=num+1
        ecol=ecol-1

        #from bottom right to bottom left
        if srow<=erow:
            for i in range(ecol,scol-1,-1):
                matrix[erow][i]=num
                num=num+1
            erow=erow-1
        #from bottom left to top left
        if scol<=ecol:
            for i in range(erow,srow-1,-1):
                matrix[i][scol]=num
                num=num+1
            scol=scol+1
    return matrix


m,n=4,4
spiral_matrix=spiral(m,n)
for i in spiral_matrix:
    print(i)