#creating the rooms
room[1]=["sign"]
r[1]="gate"
room[2]=["guard","arrow"]
r[2]="garrison quarters"
room[3]=[]
r[3]="inner courtyard"
room[4]=["blade"]
r[4]="war room"
room[5]=[]
r[5]=""
room[6]=["cross"]
r[6]="pray room"
room[7]=["hilt"]
r[7]="hallway"
room[8]=["throne","crown"]
r[8]="throne room"
room[9]=["grindtone"]
r[9]="armoury"
room[10]=["helmet"]
r[10]="hallway"
room[11]=["arrow"]
r[11]="hallway"
room[12]=["crafting_table","bow"]
r[12]="workshop"
#basic movement
def go_north(current_room):
    time.sleep(1)
    if current_room==1 or current_room==2 or current_room==3 or current_room==4:
        print("Sorry.But you can not go further north!")
    else:
        current_room=current_room-4
def go_south(current_room):
    time.sleep(1)
    if current_room==9 or current_room==10 or current_room==11 or current_room==12:
        print("Sorry.But you can not go further south!")
    else:
          current_room=current_room+4
def go_east(current_room):
    time.sleep(1)
    if current_room==4 or current_room==8 or current_room==12:
        print("Sorry,Sir.But you can not go further east!")
    else:
            current_room+=1

def go_west(current_room):
    time.sleep(1)
    if current_room==1 or current_room==5 or current_room==9:
        print("Sorry.But you noy can go further west!")
    else:
        current_room-=1
#description of the room
def look(i):
    time.sleep(1)
    i=current_room
    print("You are in the ")
    print(r[i])
    print("In this room you can see:")
    print(room[i])
#take item
def take_thing(thing,i):
    inventory.append(thing)
    room[i].remove(thing)
#use item
def use_thing(thing,i):
    if i==9 and thing="grindstone" and "sword" in inventory:
        time.sleep(1)
        inventory.remove("sword")
        inventory.append("sharp_sword")
        print("Now you are ready to kill the dragon. Run to the exit and save the kingdom, Knight.")
        else:
            if i==12 and thing="crafting_table" and "blade" in inventory and "guard" in inventory and "hilt" in inventory:
                time.sleep(1)
                inventory.remove("blade")
                inventory.remove("hilt")
                inventory.remove("guard")
                inventory.append("sword")
                print("You made the Ascalon, the legendary sword of Saint George. Now find a grindstone to make it sharp enough to kill the dragon")


    
