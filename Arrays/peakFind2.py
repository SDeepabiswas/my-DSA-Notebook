def find_peak_2d_linear(A):
    """
    A is an n x n matrix.
    Returns (row, col) of a 2D peak in O(n) time.
    """

    n = len(A)

    top, bottom = 0, n - 1
    left, right = 0, n - 1

    search_row = True   # alternate: row -> col -> row -> col

    while top <= bottom and left <= right:

        if search_row:
            mid = (top + bottom) // 2

            # find global max in row mid
            max_col = left
            for c in range(left, right + 1):
                if A[mid][c] > A[mid][max_col]:
                    max_col = c

            r, c = mid, max_col

            # check peak
            up    = A[r-1][c] if r > top else float('-inf')
            down  = A[r+1][c] if r < bottom else float('-inf')

            if A[r][c] >= up and A[r][c] >= down:
                return (r, c)

            # move toward larger vertical neighbor
            if up > A[r][c]:
                bottom = mid - 1
            else:
                top = mid + 1

        else:
            mid = (left + right) // 2

            # find global max in column mid
            max_row = top
            for r in range(top, bottom + 1):
                if A[r][mid] > A[max_row][mid]:
                    max_row = r

            r, c = max_row, mid

            # check peak
            left_val  = A[r][c-1] if c > left else float('-inf')
            right_val = A[r][c+1] if c < right else float('-inf')

            if A[r][c] >= left_val and A[r][c] >= right_val:
                return (r, c)

            # move toward larger horizontal neighbor
            if left_val > A[r][c]:
                right = mid - 1
            else:
                left = mid + 1

        search_row = not search_row   # alternate

    # fallback (should never reach for valid matrix)
    return None
A = [
    [10, 8, 10, 10,30],
    [14, 13, 12, 11,40],
    [15, 9, 11, 21,50],
    [16, 17, 19, 20,60],
    [35,36,37,38,70]
]

print(find_peak_2d_linear(A))
