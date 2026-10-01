def check_rec_mat(mat: list[list[int]]):
    """
    This function checks if the matrix is rectangular.
    """
    if not mat:
        return False
    for row in mat:
        if not isinstance(row, list):
            raise ValueError("Matrix must be a list of lists")
        if len(row) != len(mat[0]):
            return False
    return True


def check_values(mat: list[list[int]]):
    """
    This function checks if all values in the matrix are floats or integers.
    """
    for row in mat:
        for el in row:
            if not isinstance(el, (float, int)):
                raise ValueError("Matrix must contain only floats or integers")

