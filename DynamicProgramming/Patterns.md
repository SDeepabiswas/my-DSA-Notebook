# PATTERNS FOR DP

## Start from beginning and solve
**L.I.S** O(n) (subproblems) 
Each subproblem is O(m) time
 x0 x1 x2 ...xm-1 | xm
 starting point always beginning
 considering inc prefixes of complete input

## Two sequences
**EDIT DISTANCE** O(mn) (subproblems)
each problem takes O(1)

## Start at each position and do it for all
**MATRIX CHAIN MULTIPLICATION** O(n**2) (subproblems)
each position increasing length
each problem takes O(n) time

not enough to start from beginning
prefixes starting form all positions

**Independent set for a tree**
largest cardinality among all independent sets of T(ree) 