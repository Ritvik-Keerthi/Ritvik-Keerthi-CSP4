print("\nDisplaying InfoDB List now.\n")
InfoDb = []
#Append firstname, lastname, birt month, residence, and email all appended
#list within list called fav nba players, with more than 4 items
InfoDb.append({  
 "FirstName": "Ritvik",  
 "LastName": "Keerthi",  
 "DOB": "October 4",  
 "Residence": "San Diego",  
 "Email": "ritvikk53577@stu.powayusd.com",  
 "Favorite_NBAPlayers":["Chris Paul","Kawhi Leonard","Paul George","Darius Garland", "Tyrese Haliburton"]  
}) 

#Function to print data stored in InfoDb list
def print_data(n):
  InfoDb = []
#Append firstname, lastname, birt month, residence, and email all appended
#list within list called fav nba players, with more than 4 items
  InfoDb.append({  
   "FirstName": "Ritvik",  
   "LastName": "Keerthi",  
   "DOB": "October 4",  
   "Residence": "San Diego",  
   "Email": "ritvikk53577@stu.powayusd.com",  
   "Favorite_NBAPlayers":["Chris Paul","Kawhi Leonard","Paul   George","Darius Garland", "Tyrese Haliburton"]  
  }) 
  print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])
  print("\n")
  print(InfoDb[n]["DOB"])
  print("\n")
  print(InfoDb[n]["Residence"])
  print("\n")
  print(InfoDb[n]["Email"])
  print("\n")
  print("Fav NBA Players: ", end="") 
  print(", ".join(InfoDb[n]["Favorite_NBAPlayers"]))
  print()

print_data(0)