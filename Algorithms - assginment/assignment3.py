import utility
class Node:
    def __init__(self,data):
        self.l_child=None
        self.r_child=None
        self.data = data
def tree(key,r,i,j):
    k=r[i][j]
    if(k==0):
        return
    else:
        p=Node(key[k])
        p.l_child=tree(key,r,i,k-1)
        p.r_child=tree(key,r,k+1,j)
        return p
    
key=[" ","A","B","C","D","E","F"]
p=[0,3/21, 5/21, 1/21,2/21,4/21,6/21]
n=len(p)-1

a=[[0 for j in range(0,n+2)] for i in range(0,n+2)]
r=[[0 for j in range(0,n+2)] for i in range(0,n+2)]

for i in range (1,n+1):
    a[i][i-1]=0
    a[i][i]=p[i]
    r[i][i]=i
    r[i][i-1]=0
a[n+1][n]=0
r[n+1][n]=0

for d in range(1,n):
    for i in range(1,n-d+1):
        j = i+d
        sum_p = 0
        for temp in range(i,j+1):
            sum_p += p[temp]
            
        minimum = a[i][i-1] + a[i+1][j] + sum_p
        k = i+1
        count = i
        while i<= k <=j:
            if a[i][k-1] + a[k+1][j] + sum_p <= minimum:
                minimum = a[i][k-1] + a[k+1][j] + sum_p
                count = k
            k += 1
        a[i][j] = minimum
        r[i][j] = count



print("assignment 1 실행")
print()
utility.printMatrixF(a)
print()
utility.printMatrix(r)
root=tree(key,r,1,n)
utility.print_inOrder(root)
print()
utility.print_preOrder(root)
print()
print("assignment 1 실행 완료")
print()

print("assignment 2 실행")
a=['C','A','C','A','C','T','A',]
b=['T','C','A','C','T','A','C','A']
m=len(a)
n=len(b)
table=[[0 for j in range(0,n+1)] for i in range(0,m+1)]
minindex = [[ (0,0) for j in range(0,n+1)] for i in range(0,m+1)]
for j in range(n-1,-1,-1):
    table[m][j] =table[m][j+1]+2
for i in range(m-1,-1,-1):
    table[i][n] =table[i+1][n]+2

for i in range(m-1,-1,-1):
    for j in range(n-1,-1,-1):
        if a[i] == b[j]:
            p = 0
        else:
            p = 1
            
        temp1 = table[i+1][j+1] +p
        temp2 = table[i+1][j] +2
        temp3 = table[i][j+1] +2
        if min(temp1,temp2,temp3) == temp1:
            table[i][j] = temp1
            minindex[i][j] = (i+1,j+1)
        elif min(temp1,temp2,temp3) == temp2:
            table[i][j] = temp2
            minindex[i][j] = (i+1,j)
        else:
            table[i][j] = temp3
            minindex[i][j] = (i,j+1)
utility.printMatrix(table)
x=0
y=0
while (x <m and y <n):
    tx, ty = x, y
    print(minindex[x][y])
    (x,y)= minindex[x][y]
    if x == tx + 1 and y == ty+1:
        print(a[tx]," ", b[ty])
    elif x == tx and y == ty+1:
        print(" - ", " ", b[ty])
    else:
        print(a[tx], " " , " -")

print()
print("assignment 2 실행 완료")