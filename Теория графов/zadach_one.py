
# Теория графов
# Обучающие задания


'''
 Из матрицы смежности в список ребер. Некоторый граф задан матрицей смежности, выведите его представление в виде списка ребер. 
В первой строке дано число n – количество вершин в графе. В каждой следующей из n строк даны n чисел – матрица смежности графа, где «0» - отсутствие ребра, «1» - наличие ребра между вершинами.
Необходимо вывести список ребер заданного графа.
'''

def adjacent_matrix_to_edge_list(n, matrix):
    edges_list = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                edges_list.append((i, j))
    return edges_list
# Пример использования
n = int(input())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
edges_list = adjacent_matrix_to_edge_list(n, matrix)
print(edges_list)

