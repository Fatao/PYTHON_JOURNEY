# From Adjacency Matrix to Edge List

'''
Condition
Given a graph defined by an adjacency matrix, output its representation as a list of edges.

Input data
The first line of the input file contains a number n (1<=n<=100) – the number of vertices in the graph. Each of the next n lines contains n numbers, each of which is equal to 0 or 1 – the adjacency matrix of the given graph (1 means the presence of an edge, and 0 means its absence).


Output data
It is necessary to output a list of edges of a given graph.
'''
'''
Input data

5
0 0 1 0 0
0 0 1 0 1
1 1 0 0 0
0 0 0 0 0
0 1 0 0 0


Output data:
1 3
2 3
2 5
'''
n = int(input())
matrix = [] 
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)  # read the matrix

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            print(i, j)  # print the edge
            matrix[i][j] = 0
            matrix[j][i] = 0                                                                                                        
            break   