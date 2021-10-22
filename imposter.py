from termcolor import colored
import random

def display_actions(character_colour,rooms,rooms_tasks):
  counter = 1
  actions = {}

  for i in rooms:
    if character_colour in rooms[i]:
      current_room = i
      break
    else:
      continue

  while True:

    print("\nACTION")
    print("What do you want to do? You can\n")

    if len(rooms[current_room]) > 1:
      print("[{}] Kill someone".format(counter))
      actions[counter] = "kill someone"
      counter += 1

    print("[{}] Vent".format(counter))
    actions[counter] = "vent"
    counter += 1

    print("[{}] Go to new room".format(counter))
    actions[counter] = "go to new room"
    counter += 1

    if current_room == "cafeteria":
      print("[{}] Host an emergency meeting".format(counter))
      actions[counter] = "host an emergency meeting"
      counter += 1
    
    if current_room == "admin":
      print("[{}] Take a look at the map".format(counter))
      actions[counter] = "take a look at the map"
      counter += 1

    action = input("\n---> ")

    if int(action) in actions:
      return actions[int(action)]
    else:    
      print(colored("Please enter the NUMBER corresponding to the action you want to do. ","red"))
      counter = 1

def kill(imposter_room,imposter_colour,rooms):

  if len(rooms[imposter_room]) < 2:
    return False

  while True:
    killed = random.choice(rooms[imposter_room])
    if killed == imposter_colour:
      continue
    else:
      return killed

def vent():
  while True:
    print("\nWhere do you want to go? You can go to\n")
    rooms = {"1":"cafeteria","2":"weapons","3":"navigation","4":"shields","5":"storage","6":"admin","7":"electrical","8":"upper engines","9":"lower engines"}
    print("[1] Cafeteria")
    print("[2] Weapons")
    print("[3] Navigation")
    print("[4] Shields")
    print("[5] Storage")
    print("[6] Admin")
    print("[7] Electrical")
    print("[8] Upper Engines")
    print("[9] Lower Engines")
    venting = input("\n---> ")
    if venting in rooms:
      return rooms[venting]
    
