''''
Condition
Given an integer matrix, check whether it is vertically or horizontally symmetrical.

Input data
The first line contains natural numbers; n and m (1 ≤  n , m ≤10 3 ;) are the number of rows and columns of the matrix.

The next n lines contain m numbers each – the values ​​of the matrix cells (1 ≤matrix i , j  ≤10 9 ).

Output data
Print “Yes” if the matrix has vertical (a[i][j] = a[ni][j]) or horizontal (a[i][j] = a[i][mj]) symmetry, otherwise print “No”.

'''

n, m  = map(int, input().split())

matrix = []
for i in range(n):

    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(n):
    for j in range(m):
        if matrix[i][j] != matrix[n-i-1][j] and matrix[i][j] != matrix[i][m-j-1]:
            print("No")
            exit()
print("Yes")
