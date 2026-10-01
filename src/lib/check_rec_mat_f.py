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