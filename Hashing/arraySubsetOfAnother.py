def isSubset(a, b):
    # creating a hash set and inserting all elements
    # of one array, and we check if others present in the next
    hash_set = set(a)
    

    # IS b A SUBSET OF a
    for val in b:
        if val not in hash_set:
            return False
    
    return True

if __name__ == "__main__":
  a = [11, 1, 13, 21, 3, 7]
  b = [11, 3, 7, 9, 1]

  if isSubset(a, b):
      print("true")
  else:
      print("false")