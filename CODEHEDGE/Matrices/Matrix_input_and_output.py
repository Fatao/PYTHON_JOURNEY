# Matrix input and output

'''
Condition
Input and output the matrix.

Input data
The first line contains natural numbers; n and m (1 ≤  n , m ≤10 3 ;) are the number of rows and columns of the matrix.


The next n lines contain m numbers each – the values ​​of the matrix cells (1 ≤matrix i , j  ≤10 9 ).

Output data
Print n rows of m numbers – the values ​​of the matrix.

Restrictions

'''







n, m  = map(int, input().split()) 

matrix = []
for i in range(n):

    row = list(map(int, input().split()))
    matrix.append(row)

for row in matrix:
    for element in row:
        print(element, end=" ") 
    print()