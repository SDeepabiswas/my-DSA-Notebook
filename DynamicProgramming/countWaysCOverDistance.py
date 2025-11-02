# given 1 , 2 3 steps
# count the number of ways it can cover the input

def count(dist):

    ways = [0]*3

    ways[0] = 1
    ways[1] = 1
    ways[2] = 2

    for i in range(3, (dist)+1):
        ways [i % 3 ] = ways [(i-1) % 3] + ways [(i-2) % 3] + ways [(i-3) % 3]

    return ways [dist % 3]

if __name__ == "__main__":
    dist = 4
    print(count (dist))