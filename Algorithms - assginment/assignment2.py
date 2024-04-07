def allShortestPath (g,n):
# node number는 1 부터 n

    d = [[0 for j in range(0,n)] for i in range(0,n)]
    p = [[0 for j in range(0,n)] for i in range(0,n)]
    d = g
    for k  in range(0,n):
        for i in range(0,n):
            for j in range(0,n):
                if d[i][k] + d[k][j] < d[i][j]:
                    p[i][j] = k + 1;
                    d[i][j] = d[i][k] + d[k][j]
    return d,p

def printMatrix (d):
    n= len (d[0])
    for i in range(0,n):
        for j in range(0,n):
            print(d[i][j], end=" ")
        print()

def path(p,q,r):
    q -=1
    r-=1
    if p[q][r] != 0:
        path(p,q,p[q][r])
        print("v" + str(p[q][r]), end='')
        path(p,p[q][r],r)
        

print("assignment 1 실행")
inf = 1000
g=[[0,3,inf,4,inf],  
[inf,0,1,inf,inf],
[inf,9,0,2,3],
[3,1,inf,0,2],
[inf,inf,inf,4,0]]
d, p =  allShortestPath (g,5)
print()
printMatrix(d)
print()
printMatrix(p)
print()

print("v1 >> ", end='')
path(p,1,5)
print(" >> v5")
print()

print("assignment 1 실행 완료")


def order(p,i,j):
    if i == j:
        print("A" +str(i)+" ",end="")
    else:
        k = p[i-1][j-1]+1
        print("(",end="")
        order(p,i,k)
        order(p,k+1,j)
        print(")",end="")
    return

d=[3,4,6,5,8,2]
n=len(d)
m=[[0 for j in range(1,n+1)] for i in range(1,n+1)]
p=[[0 for j in range(1,n+1)] for i in range(1,n+1)]


for diagonal in range(1,n):
    for i in range(1, n-diagonal):
        j = i +diagonal 
        minimum = m[i][i]+m[i+1][j] + d[i-1]*d[i]*d[j]
        k = i +1
        temp = i
        while(i<= k <=j-1):
        
            if m[i][k]+m[k+1][j] + d[i-1]*d[k]*d[j] <= minimum:
                minimum = m[i][k]+m[k+1][j] + d[i-1]*d[k]*d[j]
                temp = k

            k += 1
        m[i][j] = minimum
        p[i][j] = temp

print()
print("assignment 2 실행")
print()
printMatrix(m)
print()
printMatrix(p)
order(p,1,6)
print()
print()
print("assignment 2 실행 완료")