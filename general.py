from termcolor import colored
import random, time, os

def display_information(character_colour,character_status,rooms,rooms_task):
  os.system("clear")
  print("INFORMATION")
  print("You are " + colored(character_colour,character_colour) + " and you are {}.".format(character_status))
  
  for i in rooms:
    if character_colour in rooms[i]:
      print("You are in {}. The other people in this room are: ".format(i),end="")
      for j in rooms[i]:
        if j !=  character_colour:
          print(colored("{} ".format(j),j),end="")
        else:
          continue
      break
    else:
      continue
  

  print("\n\nThe remaining tasks for the crewmates to complete are:")
  for i in rooms_task:
    print(colored("\n{}:".format(i),character_colour),end="")
    for j in rooms_task[i]:
      print(" {} |".format(j),end="")
  print("")
  


def meeting(imposter_colour,character_colour,suspicion,colours):

  vote_number = {}
  vote_number_lookup = {}

  for i in range(len(colours)):
    vote_number[colours[i]] = 0

  for i in range(0,len(colours)):
    vote_number_lookup[i] = colours[i]
  
  print("\nEMERGENCY MEETING")
  print("Who do you vote for?")
  for i in range(len(colours)):
    print("{} - {}".format(i+1,colours[i]))
  while True:
    voting = input("---> ")
    if voting in ["1","2","3","4","5","6"]:
      vote_number[vote_number_lookup[int(voting)-1]] += 1
      break
    else:
      print("Please enter the NUMBER corresponding to the person you want to vote off.")
  
  for i in range(len(colours) - 1):
    while True:
      voting = random.randint(0,len(colours)+suspicion-1)
      if voting in range(0,suspicion):
        vote_number[character_colour] += 1
        break
      else:
        if vote_number_lookup[int(voting-suspicion)] == character_colour:
          continue
        vote_number[vote_number_lookup[int(voting)-suspicion]] += 1
        break

  time.sleep(2)

  print("\nVOTING RESULTS")
  for i in colours:
    print(colored("{}: {}".format(i,vote_number[i]),i))
  
  ejected = []
  max = 0
  for colour, voteCount in vote_number.items():
    if voteCount == max:
      ejected.append(colour)
    elif voteCount > max:
      ejected = [colour]
      max = voteCount
    
  time.sleep(2)

  if len(ejected) == 1:

    if ejected[0] in colours: 
      print("{} HAS BEEN EJECTED".format(ejected[0].upper()))
      time.sleep(1)
      if imposter_colour == ejected[0]:
        print(colored("{} WAS THE IMPOSTER".format(ejected[0].upper()),"red"))
        time.sleep(1)
        if character_colour == imposter_colour:
          print(colored("DEFEAT","red"))
          quit(0)
        else:
          print(colored("VICTORY","green"))
          quit(0)
      else:
        print(colored("{} WAS NOT THE IMPOSTER\n".format(ejected[0].upper()),"green"))
        time.sleep(1)
        return ejected[0]
    
  else:
    print("NO ONE WAS EJECTED\n")
    time.sleep(2)
    return False

def change_rooms(character_colour,rooms):

  available_room = {}

  for i in rooms:
    if character_colour in rooms[i]:
      current_room = i
      break
    else:
      continue
  
  while True:
    print("\nWhich room do you want to go to? You can go to\n")

    if current_room == "cafeteria":
      print("[1] Weapons")
      print("[2] Storage")
      print("[3] Admin")
      print("[4] Upper Engines")
      available_room = {"1":"weapons","2":"storage","3":"admin","4":"upper engines"}
    elif current_room == "weapons":
      print("[1] Cafeteria")
      print("[2] Shields")
      print("[3] Navigation")
      available_room = {"1":"cafeteria","2":"shields","3":"navigation"}
    elif current_room == "navigation":
      print("[1] Weapons")
      print("[2] Shields")
      available_room = {"1":"weapons","2":"shields"}
    elif current_room == "shields":
      print("[1] Navigation")
      print("[2] Weapons")
      print("[3] Storage")
      available_room = {"1":"navigation","2":"weapons","3":"storage"}
    elif current_room == "storage":
      print("[1] Cafeteria")
      print("[2] Shields")
      print("[3] Admin")
      print("[4] Electrical")
      print("[5] Lower Engines")
      available_room = {"1":"cafeteria","2":"shields","3":"admin","4":"electrical","5":"lower engines"}
    elif current_room == "admin":
      print("[1] Cafeteria")
      print("[2] Storage")
      available_room = {"1":"cafeteria","2":"storage"}
    elif current_room == "electrical":
      print("[1] Storage")
      print("[2] Lower Engines")
      available_room = {"1":"storage","2":"lower engines"}
    elif current_room == "lower engines":
      print("[1] Upper Engines")
      print("[2] Electrical")
      print("[3] Storage")
      available_room = {"1":"upper engines","2":"electrical","3":"storage"}
    elif current_room == "upper engines":
      print("[1] Cafeteria")
      print("[2] Lower Engines")
      available_room = {"1":"cafeteria","2":"lower engines"}


    changing_room = input("\n---> ")

    if changing_room in available_room:
      return available_room[changing_room]
    else:
      print(colored("Please enter the NUMBER corresponding to the room you want to enter.","red"))