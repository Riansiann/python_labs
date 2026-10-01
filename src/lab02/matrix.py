from src.lib.check_mat_values_f import check_values
from src.lib.check_rec_mat_f import check_rec_mat

def transpose(mat: list[list[int]]) -> list[list[int]]:
    """
    This function transposes the given matrix.
    """
    if len(mat) == 0:
        return []
    if not check_rec_mat(mat):
        raise ValueError("Matrix is not rectangular")
    check_values(mat)
    new_mat = []
    for i in range(len(mat[0])):
        new_row = []
        for j in range(len(mat)):
            new_row.append(mat[j][i])
        new_mat.append(new_row)
    return new_mat

#test cases
print(transpose([[1,2,3]]))
print(transpose([[1],[2],[3]]))
print(transpose([[1,2], [3,4]]))
print(transpose([]))
print(transpose([[1,2],[3]]))

def row_sums(mat: list[list[float|int]]) -> list[float]:
    """
    This function calculates the sum of each row in the given matrix.
    """
    if not check_rec_mat(mat):
        raise ValueError("Matrix is not rectangular")
    check_values(mat)
    res = [sum(row) for row in mat]
    return res

#test cases
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1,1], [10,-10]]))
print(row_sums([[0,0], [0,0]]))
print(row_sums([[1, 2], [3]]))

def col_sums(mat: list[list[float|int]]) -> list[float]:
    """
    This function calculstes the sum of each column in the given matrix.
    """
    if not check_rec_mat(mat):
        raise ValueError("Matrix is not rectangular")
    check_values(mat)
    res = [sum(row[i] for row in mat) for i in range(len(mat[0]))]
    return res

#test cases
print(col_sums([[1, 2,3], [4,5,6]]))
print(col_sums([[-1,1], [10,-10]]))
print(col_sums([[0,0], [0,0]]))
print(col_sums([[1, 2], [3]]))
