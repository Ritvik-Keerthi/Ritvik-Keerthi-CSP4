global number1
global number2
def Swap(number1, number2):
  # age1 = input("age 1 :")
  # age2 = input("age 2 :")
  if(number1 > number2):
    temp = number1 
    temp = number2
    number1 = number2
    number2 = temp
  return(number1, number2)

def swapTester():
  number1 = int(input("number 1 :"))
  number2 = int(input("number 2 :"))
  number1, number2 = Swap(number1, number2)
  print("number 1 = " + str(number1),"number 2 = " + str(number2))
  
