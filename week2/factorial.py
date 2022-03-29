
class Factorial:
  def __init__(self, num):
    self.num = num 
  def __call__(self):
    if self.num == 1:
      return self.num
    if self.num < 0:
      print("No factorial for this number")
    else:
      n = 1
      for i in range (1,int(self.num)+1):
        n = n*i
        print(i, ":", n)
      print("The factorial of", self.num, "is", n) 
        
def factorial_print():
  inp = int(input("Enter a number you want the factorial of: "))
  p1 = Factorial(inp)
  p1()

def seq_sum():
  num = int(input("Enter a number for your sequential sum: "))
  n = 0
  if num <= 0:
    print("This number has no sequence sum")
  else:
    for i in range(1, num + 1):
      n = n + i
    print("The sum of all numbers starting from 1 to", num, "is", n)
