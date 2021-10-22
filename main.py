from termcolor import colored
import random, time, os
import imposter, crewmate, general, bot

#Globals 

colours = ["red","yellow","green","cyan","blue","magenta"]
rooms = {
  "cafeteria":["red","yellow","green","cyan","blue","magenta"],
  "weapons":[],
  "navigation":[],
  "shields":[],
  "storage":[],
  "admin":[],
  "electrical":[],
  "lower engines":[],
  "upper engines":[],
}
rooms_tasks = {
  "cafeteria":["empty garbage","fix wiring","buy drink"],
  "weapons":["destroy asteriods","download data"],
  "navigation":["stabilize steering","fix wiring","download data"],
  "shields":["download data"],
  "storage":["fix wiring","empty garbage"],
  "admin":["card swipe","upload data"],
  "electrical":["fix wiring","download data"],
  "lower engines":["download data"],
  "upper engines":["download data"],
}


#Game functions

def main():
  while True:
    action = input("What would you like to do?\n1 - Play singleplayer\n---> ")
    if action == "1":
      os.system("clear")
      time.sleep(1)
      single_player()
    else:
      print("Please enter the NUMBER corresponding to the action you want to do. ")

def single_player():
  #Setup
  character_colour = random.choice(colours)
  imposter_colour = random.choice(colours)

  if imposter_colour == character_colour:
    character_status = "imposter"
  else:
    character_status = "crewmate"
  
  #Setting cooldowns
  meeting_cooldown = 4
  kill_cooldown = 5

  suspicion = 1

  #Game loop
  while True:
    
    #Verify different stuff

    #Verifying character isn't dead
    if character_colour in colours:
      pass
    else:
      print("YOU DIED (either by getting ejected or getting killed by the imposter)")
      print(colored("DEFEAT","red"))
      quit(0)

    #Verify not all tasks are completed
    rooms_tasks_num = 0
    for i in rooms_tasks:
      if len(rooms_tasks[i]) == 0:
        rooms_tasks_num += 1
    if rooms_tasks_num == len(rooms_tasks):
      print("ALL TASKS ARE COMPLETED")
      if character_status == "crewmate":
        print(colored("VICTORY","green"))
        quit(0)
      elif character_status == "imposter":
        print(colored("DEFEAT","red"))
        quit(0)

    #If imposter, verify that there isn't 2 people left
    if character_status == "imposter":
      if len(colours) <= 2:
        print("YOU KILLED EVERYONE")
        print(colored("VICTORY","green"))
        quit(0)
    elif character_status == "crewmate":
      if len(colours) <= 2:
        print("THE IMPOSTER KILLED EVERYONE")
        print(colored("DEFEAT","red"))
        quit(0)

    #Update information
    for i in rooms:
      if character_colour in rooms[i]:
        current_room = i
        break
      else:
        continue

    #Display information
    general.display_information(character_colour,character_status,rooms,rooms_tasks)


    #Do something
    if character_status == "crewmate":
      crewmate_action = crewmate.display_actions(character_colour,rooms,rooms_tasks)
      if crewmate_action == "do tasks":
        task_done = crewmate.do_tasks(character_colour,rooms,rooms_tasks)  
        rooms_tasks[current_room].remove(task_done)
      elif crewmate_action == "go to new room":
        changed_room = general.change_rooms(character_colour,rooms)
        rooms[current_room].remove(character_colour)
        rooms[changed_room].append(character_colour)
      elif crewmate_action == "host an emergency meeting":
        if meeting_cooldown > 0:
          print(colored("Try again in {} turns.".format(meeting_cooldown),"red"))
          time.sleep(1)
          continue
        ejected = general.meeting(imposter_colour,character_colour,suspicion,colours)
        meeting_cooldown = 4
        if ejected in colours:
          colours.remove(ejected)
          for i in rooms:
            if ejected in rooms[i]:
              rooms[i].remove(ejected)
              break
            else:
              continue
      elif crewmate_action == "take a look at the map":
        print("\nMAP",end="")
        for i in rooms:
          print("\n{}: ".format(i),end="")
          for j in rooms[i]:
            print(colored("{} ".format(j),j),end="")
        
        while True:
          what_to_do = input("\n\nEnter 'q' to quit the map. ")
          if what_to_do == "q":
            break
          else:
            continue
        
        


    elif character_status == "imposter":
      imposter_action = imposter.display_actions(character_colour,rooms,rooms_tasks)
      for i in rooms:
        if imposter_colour in rooms[i]:
          imposter_room = i
          break
      if imposter_action == "kill someone":
        if kill_cooldown > 0:
          print(colored("Try again in {} turns.".format(kill_cooldown),"red"))
          time.sleep(2)
          continue
        killed = imposter.kill(imposter_room,imposter_colour,rooms)
        if killed in colours:
          print("You killed {}".format(killed))
          time.sleep(2)
          colours.remove(killed)
          for i in rooms:
            if killed in rooms[i]:
              rooms[i].remove(killed)
              break
          suspicion += len(rooms[current_room]) - 1
          kill_cooldown = 5
      elif imposter_action == "vent":
        changed_room = imposter.vent()
        rooms[current_room].remove(character_colour)
        rooms[changed_room].append(character_colour)
        suspicion += len(rooms[current_room])
        suspicion += len(rooms[changed_room])-1
      elif imposter_action == "go to new room":
        changed_room = general.change_rooms(character_colour,rooms)
        rooms[current_room].remove(character_colour)
        rooms[changed_room].append(character_colour)
      elif imposter_action == "host an emergency meeting":
        if meeting_cooldown > 0:
          print(colored("Try again in {} turns.".format(meeting_cooldown),"red"))
          time.sleep(1)
          continue
        ejected = general.meeting(imposter_colour,character_colour,suspicion,colours)
        meeting_cooldown = 4
        if ejected in colours:
          colours.remove(ejected)
          for i in rooms:
            if ejected in rooms[i]:
              rooms[i].remove(ejected)
              break
            else:
              continue
      elif imposter_action == "take a look at the map":
        print("\nMAP",end="")
        for i in rooms:
          print("\n{}: ".format(i),end="")
          for j in rooms[i]:
            print(colored("{} ".format(j),j),end="")
        
        while True:
          what_to_do = input("\n\nEnter 'q' to quit the map. ")
          if what_to_do == "q":
            break
          else:
            continue


      
    #Bot crewmates action
    for i in colours:
      bot_crewmate_action = random.randint(0,10)
      #Confirm this isn't the player
      if i == character_colour:
        continue
      else:
        #Finding where the room is
        for j in rooms:
          if i in rooms[j]:
            bot_crewmate_room = j
            break
        #Checking if bot can do task
        if len(rooms_tasks[bot_crewmate_room]) > 0:
          if bot_crewmate_action in range(0,3):
            task_done = random.choice(rooms_tasks[bot_crewmate_room])
            rooms_tasks[bot_crewmate_room].remove(task_done)
          else:
            pass
        
        if bot_crewmate_action in range(3,7):
          bot_changed_room = bot.change_rooms(i,rooms)
          rooms[bot_crewmate_room].remove(i)
          rooms[bot_changed_room].append(i)
        elif bot_crewmate_action in range(7,10):
          pass


        
      
      
    #Bot imposter action
    if character_status == "crewmate":
      #Finding where imposter room is
      for i in rooms:
        if imposter_colour in rooms[i]:
          imposter_room = i
          break
      #Bot imposter does something
      bot_imposter_action = random.randint(0,10)


      if bot_imposter_action in range(0,3):
        rooms[imposter_room].remove(imposter_colour)
        imposter_room = random.choice(["cafeteria","weapons","navigation","shields","storage","electrical","lower engines","upper engines"])
        rooms[imposter_room].append(imposter_colour)
      elif bot_imposter_action in range(4,10):
        killed = imposter.kill(imposter_room,imposter_colour,rooms)
        if killed in colours:
          colours.remove(killed)
          for i in rooms:
            if killed in rooms[i]:
              rooms[i].remove(killed)
              break
          
    if suspicion > 2:
      print("\nYour suspicion level is {}, which is over 2, so the humans called an emergency meeting.".format(suspicion))
      time.sleep(2)
      ejected = general.meeting(imposter_colour,character_colour,suspicion,colours)
      if ejected in colours:
        colours.remove(ejected)
        for i in rooms:
          if ejected in rooms[i]:
            rooms[i].remove(ejected)
            break
          else:
            continue
      suspicion -= 1
      

    #Update cooldowns
    meeting_cooldown -= 1
    kill_cooldown -= 1

      
main()

