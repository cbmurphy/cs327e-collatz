#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2013
# Glenn P. Downing
# ---------------------------

hashTable = {}

# ------------
# collatz_read
# ------------

def collatz_read (r, a) :
    """ reads two ints into a[0] and a[1] r is a  reader a is an array
    of int return true if that succeeds, false otherwise """
    try:
        s = r.readline()
        l = s.split()
        a[0] = int(l[0])
        a[1] = int(l[1])
        assert a[0] > 0
        assert a[1] > 0
        return True
    except:
        return False

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    note: i need not be less than j
    return the max cycle length in the range [i, j]
    """
    assert i > 0
    assert j > 0
    highCount = 0
    if i > j:
        i, j = j, i
    for x in range(i, j + 1):
      hashArray = {}
      startNum = x
      count = 0
      while (x > 1):
        if x in hashTable:
            count += hashTable[x]
            break
        elif (x % 2) == 0:
          x //= 2
        else:
          x = x * 3 + 1
        count += 1
      hashTable[startNum] = count
      count += 1
      if count > highCount:
        highCount = count
    assert highCount > 0
    return highCount

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    prints the values of i, j, and v
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    a = [0, 0]
    while collatz_read(r, a) :
        v = collatz_eval(a[0], a[1])
        collatz_print(w, a[0], a[1], v)
    return 0

if __name__ == "__main__":
    collatz_solve(sys.stdin, sys.stdout)
