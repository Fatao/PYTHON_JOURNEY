# From Adjacency Matrix to Edge List

'''
Condition
Given an adjacency matrix of a graph, output the edge list.

Input data  
The first line contains a natural number n (1 ≤ n ≤ 100) - the number of vertices in the graph.

The next n lines contain n numbers each - the elements of the adjacency matrix of the graph. The matrix is symmetric with respect to the main diagonal.

Output data 
Print the edges of the graph in the form of a list of pairs of vertices. The edges can be printed in any order.
'''


n = int(input())
matrix = [] 
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            print(i, j)
            matrix[i][j] = 0
            matrix[j][i] = 0
            break
# Compare this snippet from CODEHEDGE/MODULE%204/COUNT%20BASE/magnetic_puzzles.py: