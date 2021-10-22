from termcolor import colored
import random, time, os

def change_rooms(bot_colour,rooms):

  for i in rooms:
    if bot_colour in rooms[i]:
      current_room = i
      break

  if current_room == "cafeteria":
    available_room = ["weapons","storage","admin","upper engines"]
  elif current_room == "weapons":
    available_room = ["cafeteria","shields","navigation"]
  elif current_room == "navigation":
      available_room = ["weapons","shields"]
  elif current_room == "shields":
    available_room = ["navigation","weapons","storage"]
  elif current_room == "storage":
    available_room = ["cafeteria","shields","admin","electrical","lower engines"]
  elif current_room == "admin":
    available_room = ["storage","cafeteria"]
  elif current_room == "electrical":
    available_room = ["storage","lower engines"]
  elif current_room == "lower engines":
    available_room = ["upper engines","electrical","storage"]
  elif current_room == "upper engines":
    available_room = ["cafeteria","lower engines"]

  changed_room = random.choice(available_room)
  return changed_room