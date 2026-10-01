def check_values(mat: list[list[int]]):
    """
    This function checks if all values in the matrix are floats or integers.
    """
    for row in mat:
        for el in row:
            if not isinstance(el, (float, int)):
                raise ValueError("Matrix must contain only floats or integers")