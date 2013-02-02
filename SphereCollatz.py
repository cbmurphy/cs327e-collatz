#!/usr/bin/env python3
import sys
hashTable = {}
def collatz_read (r, a) :
    try:
        s = r.readline()
        l = s.split()
        a[0] = int(l[0])
        a[1] = int(l[1])
        return True
    except:
        return False
    
def collatz_eval (i, j) :
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
    return highCount

def collatz_print (w, i, j, v) :

    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

def collatz_solve (r, w) :
    a = [0, 0]
    while collatz_read(r, a) :
        v = collatz_eval(a[0], a[1])
        collatz_print(w, a[0], a[1], v)
    return 0

x = 0
for y in range(1000,1000000, 1000):
    collatz_solve(x, y)
    x = y


collatz_solve(sys.stdin, sys.stdout)

