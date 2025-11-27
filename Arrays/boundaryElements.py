def print_boundary(a):
    m, n = len(a), len(a[0])
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                print(a[i][j], end=' ')
            else:
                print('  ', end='') # Two spaces for inner empty elements
        print() 

# Driver code
if __name__ == '__main__':
    a = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [0, 2, 3, 4],
        [5, 6, 7, 8]
    ]
    print_boundary(a)