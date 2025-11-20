def find_peak_2d(A):
    """
    A is an n x m matrix (list of lists).
    Returns coordinates (row, col) of a 2D peak.
    """

    n = len(A)
    m = len(A[0])

    def get_col_max(col):
        # returns (row_index, value)
        max_row = 0
        max_val = A[0][col]
        for r in range(1, n):
            if A[r][col] > max_val:
                max_val = A[r][col]
                max_row = r
        return max_row, max_val

    def peak_find(L, R):
        # search columns L..R (inclusive)
        if L == R:
            r, _ = get_col_max(L)
            return r, L

        mid = (L + R) // 2
        r, val = get_col_max(mid)

        left_val  = A[r][mid - 1] if mid - 1 >= L else float('-inf')
        right_val = A[r][mid + 1] if mid + 1 <= R else float('-inf')

        # check if peak
        if val >= left_val and val >= right_val:
            return r, mid

        # move where larger neighbor is
        if left_val > val:
            return peak_find(L, mid - 1)
        else:
            return peak_find(mid + 1, R)

    return peak_find(0, m - 1)
A = [
    [10, 8, 10, 10],
    [14, 13, 12, 11],
    [15, 9, 11, 21],
    [16, 17, 19, 20]
]

print(find_peak_2d(A))
