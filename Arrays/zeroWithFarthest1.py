import math


def maxDistToClosest(seats):

    # Initialize the maximum distance to -1
    res = -1

    # Initialize a variable to count consecutive empty seats
    emptyCnt = 0

    # Iterate through the binary string 'seats'
    for i in range(len(seats)):
        if seats[i] == '0':

            # Increment the count for consecutive empty seats
            emptyCnt += 1

        elif seats[i] == '1' and res == -1:

            # Update 'res' with 'emptyCnt' if it's the first occupied seat
            res = emptyCnt
            # Reset the count of consecutive empty seats
            emptyCnt = 0

        else:

            # Update 'res' with half of 'emptyCnt' if not the first occupied seat
            res = max(res, math.ceil(
                emptyCnt / 2))

            # Reset the count of consecutive empty seats
            emptyCnt = 0

    # Update 'res' one more time after the loop
    # for any consecutive empty seats at the end
    res = max(res, emptyCnt)

    return res


# Driver code
seats = '1000101'

# Calling and printing the result
print(maxDistToClosest(seats))