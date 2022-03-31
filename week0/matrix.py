global list

def matrix(list):
  for i in list:
         print(*i)

#Tried user input here but I don't think it's right
def matrixTester():
  rows = int(input("How many rows: "))
  list = []
  for i in range(0,rows):
    inner = input("List inner values for row " + str(i + 1) +": ")
    list.append(inner)
  if(',' in list ):
    list.sub(',')
  matrix(list)

def matrixTester2():
  list = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
  print(matrix(list))