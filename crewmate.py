from termcolor import colored
import time, random, os

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

    if len(rooms_tasks[current_room]) != 0:
      print("[{}] Do tasks in {}".format(counter,current_room))
      actions[counter] = "do tasks"
      counter += 1

    print("[{}] Go to a new room".format(counter))
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


def do_tasks(character_colour,rooms,rooms_tasks):

  counter = 1

  for i in rooms:
    if character_colour in rooms[i]:
      current_room = i
      break
    else:
      continue
    
  while True:
    tasks = {}
    print("\nWhat task would you like to complete? You can do\n")
    for i in rooms_tasks[current_room]:
      print("[{}] {}".format(counter,i))
      tasks[counter] = i
      counter += 1

    task = input("\n---> ")
    if int(task) in tasks:
      if tasks[int(task)] == "empty garbage":
        empty_garbage()
        return "empty garbage"
      elif tasks[int(task)] == "fix wiring":
        fix_wiring()
        return "fix wiring"
      elif tasks[int(task)] == "destroy asteriods":
        destroy_asteriods()
        return "destroy asteriods"
      elif tasks[int(task)] == "card swipe":
        card_swipe()
        return "card swipe"
      elif tasks[int(task)] == "buy drink":
        buy_drink()
        return "buy drink"
      elif tasks[int(task)] == "stabilize steering":
        stabilize_steering()
        return "stabilize steering"
      elif tasks[int(task)] == "download data":
        download_data()
        return "download data"
      elif tasks[int(task)] == "upload data":
        upload_data()
        return "upload data"
    else:
      print(colored("\nPlease enter the NUMBER corresponding to the task you would you like to complete.","red"))
      counter = 1





#Tasks
def destroy_asteriods():
  print("\nTASK: Destroy Asteriods")
  print(colored("Destroy asteriods that will crash into the ship! ","blue"))
  for i in range(3):
    random_x = random.randint(0,2)
    random_y = random.randint(0,2)
    print(colored("One asteriod at ({},{})".format(random_x,random_y),"red"))
    while True:
      coordinate = input(colored("Type in ({},{}) to destroy the asteriod. ".format(random_x,random_y),"red"))
      if coordinate == "({},{})".format(random_x,random_y):
        print(colored("You hit the asteriod!","green"))
        break
  print("TASK COMPLETED")
  time.sleep(1)
  return True


def card_swipe():
  print("\nTASK: Card Swipe")
  print(colored("Swipe the card and pray you pass.","blue"))
  while True:
    card = input(colored("Type in 'SWIPE' ","red"))
    if card == "SWIPE":
      pass_ = random.choice(["pass","fail"])
      if pass_ == "pass":
        print(colored("You passed!","green"))
        break
      elif pass_ == "fail":
        continue


def buy_drink():
  print("\nTASK: Buy drink")
  print(colored("Order the correct drink! ","blue"))
  choices = ["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
  choice = random.choice(choices)
  while True:
    drink = input(colored("Type in {} to order the drink. ".format(choice),"red"))
    if drink == "{}".format(choice):
      print(colored("You ordered the correct drink! ","green"))
      break
  print("TASK COMPLETED")
  time.sleep(1)
  return True


def empty_garbage():
  print("\nTASK: Empty garbage")
  print(colored("Empty the garbage in the ship! ","blue"))
  for i in range(3):
    random_time = random.randint(1,3)
    time.sleep(random_time)
    while True:
      typed = input(colored("Type in 'EMPTY'! ","red"))
      if typed == "EMPTY":
        print(colored("Garbage emptied! ({} more times left)".format(2-i),"green"))
        break
  print("TASK COMPLETED")
  time.sleep(1)
  return True

def enter_code():
  print("\nTASK: Enter code")
  print(colored("Enter the correct code to pass! ","blue"))
  code = random.randint(100000,999999)
  while True:
    typed = input(colored("Type in {} ".format(code),"red"))
    if typed == str(code):
      break
  print("TASK COMPLETED")
  time.sleep(1)
  return True

def fix_wiring():
  print("\nTASK: Fix wiring")
  print(colored("Fix the wiring on a panel! ","blue"))
  #Setup panel
  colours = ["red","yellow","blue","purple"]
  panel = []
  for i in range(4):
    colour = random.choice(colours)
    panel.append(colour)
    colours.remove(colour)
  #Task
  print(colored("This panel has \n1 - {}\n2 - {}\n3 - {}\n4 - {}".format(panel[0],panel[1],panel[2],panel[3]),"magenta"))
  for i in range(4):
    while True:
      typed = input(colored("What is the colour corresponding to number {}? ".format(i+1),"red"))
      if typed == panel[i]:
        print(colored("Correct! ({} more colours left)".format(3-i),"green"))
        break
  print("TASK COMPLETED")
  time.sleep(1)
  return True



def stabilize_steering():
  print("\nTASK: Stabilize steering")
  print(colored("Make sure you're steering in the right direction!","blue"))
  random_x = random.randint(-5,6)
  random_y = random.randint(-5,6)
  while True:
    thing = input(colored("Type in ({},{}) to stabilize steering. ".format(random_x,random_y),"red"))
    if thing == "({},{})".format(random_x,random_y):
      break
    else:
      continue
  print("TASK COMPLETED")
  time.sleep(1)
  return True
  

def download_data():
  print("TASK: Download data")
  print(colored("Download the data!","blue"))
  print("Downloading...")
  time.sleep(3)
  passcode = random.randint(100,999)
  while True:
    password = input(colored("Type in {} to confirm download. ".format(passcode),"red"))
    if int(password) == passcode:
      print(colored("Correct!","green"))
      break
    else:
      continue
  print("Confirming...")
  time.sleep(2)
  print("TASK COMPLETED")
  time.sleep(1)
  return True
    

def upload_data():
  print("TASK: Upload data")
  print(colored("Upload the data!","blue"))
  print("Uploading... (this may take some time)")
  time.sleep(5)
  time_ = random.randint(1,4)
  print("Deleting data...")
  time.sleep(time_)
  print("TASK COMPLETED")
  time.sleep(1)
  return True

