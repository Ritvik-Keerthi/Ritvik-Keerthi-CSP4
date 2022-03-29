InfoDbLoop = []

InfoDbLoop.append({  
              "FirstName": "Ritvik",  
              "LastName": "Keerthi",  
              "DOB": "October 4",  
              "Residence": "San Diego",   
              "Favorite_NBAPlayers":["Chris Paul","Kawhi Leonard","Paul George","Darius Garland", "Tyrese Haliburton"] 
              })  

def print_data(n):
  print(InfoDbLoop[n]["FirstName"])  # print name
  print("\t", "DOB: ", end="")
  print(InfoDbLoop[n]["DOB"])
  print("\t", "Residence: ", end="")
  print(InfoDbLoop[n]["Residence"])
  print("\t", "Favorite NBA Players: ", end="")
  print(", ".join(InfoDbLoop[n]["Favorite_NBAPlayers"]))
  print()



# For Loop
def for_loop():
  for n in range(len(InfoDbLoop)):
    print_data(n)

# While Loop
# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
  while n < len(InfoDbLoop):
    print_data(n)
    n += 1
  return

# Recursion
# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop(n):
  if n < len(InfoDbLoop):
    print_data(n)
    recursive_loop(n + 1)
  return # exit condition

def main():
  print("For Loop")
  for_loop()
  print("While loop")
  while_loop(0)
  print("Recursion")
  recursive_loop(0)