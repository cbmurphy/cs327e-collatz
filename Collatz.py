hashTable = {}

def main():

  '''main function to get input and print results'''
  
  #get input and print result
  while True:
    x = [int(x) for x in input().split()]
    if x:
      print(x[0], x[1], result(x[0], x[1]))
    else:
      break

  return 0

def result(i, j):

  '''function to compute result of given pairs of numbers'''

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

main()
