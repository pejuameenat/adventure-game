import time
import random

random_creatures = ["troll", "pirate", "gorgon", "pixie", "vampire"]
creature = random.choice(random_creatures)
random_weapons = ["sword of ogoroth!", "axe of fury!", "whip of hercules!","shackles of fire!!"]
weapon = random.choice(random_weapons)
fight_weapon = []

#  for intervals in printing messages
def pause_interval(message):
    print(message)
    time.sleep(2)

def decision():
    while True:
        answer = input("what would you like to (1) fight (2) run away?")
        if "1" in answer:
            fight()
            break
        elif "2" in answer:
            enter_field() 

# # decisions to make 
# # you fight!  
def fight():
    while True:
        if weapon in fight_weapon:
            pause_interval(f"As the {creature} moves to attack, you unsheath your new {weapon}")
            pause_interval(f"The {weapon} shines brightly in your hands as you brace yourself for the attack")
            pause_interval(f"But the {creature} takes a look at your {weapon} and runs away!")
            pause_interval(f"You have rid the town of the {creature} and are victorious!")
            # break
        else: 
            pause_interval(f"You tried your best.. \nbut your tiny dagger was no match for the {creature}.\nYou have been defeated!")
        while True:
            response = input("would you like to play again? yes/no?: ")   
            if "yes" in response:
                pause_interval("Excellent! restarting the game..")
                start()
                options()
                break
            elif "no" in response: 
                pause_interval("Thanks for playing! see you next time")
                break
            else: 
                pause_interval("I dont understand")
        break 

# #run for your life!
def enter_field():
    pause_interval(f"You run back to the field luckily, you don't seem to be followed")
    options()  

# # entering the house
def enter_house():
    if weapon in fight_weapon:
        pause_interval("You approach the front door")
        pause_interval(f"You are about to knock when the door opens and out steps a {creature}")  
        pause_interval(f"Eep! this is the {creature}'s house!\nthe {creature} attacks you!")
        pause_interval("You feel a bit underprepared for this, with only having  a tiny dagger ")
    decision()

def enter_cave():
    pause_interval("You peer cautiously into the cave")
    pause_interval("it turns out to be only a very small cave")
    pause_interval("Your eye catches a glint of metal behind the rock")
    pause_interval(f"You have found the magical {weapon}!")
    pause_interval(f"You discard your silly old dagger and take the {weapon} with you")
    pause_interval(f"You walk back out to the field")
    if weapon not in fight_weapon:
        fight_weapon.append(weapon)
        pause_interval("You can now proceed to fight!") 
    decision()
    
def start():
    pause_interval(f"You find yourself standing in an open field, filled with grass and yellow wildflowers") 
    pause_interval(f"Rumor has it that a wicked {creature} is somewhere around here, and has been terrifying the nearby village.")
    pause_interval(f"In front of you is a house.")
    pause_interval(f"To your right is a dark cave")
    pause_interval(f"In your hand you hold your trusty (but not very effective) dagger.")
start()

# # options to choose from
def options():
    pause_interval(f"\nEnter 1 to knock on the door of the house.") 
    pause_interval(f"Enter 2 to peer into the cave.") 
    pause_interval(f"What would you like to do?") 
    while True:
        answer_opt = input(f"(Please enter 1 or 2):\n")
        if "1" in answer_opt:
            enter_house()
            break
        elif "2" in answer_opt:
            enter_cave()
            break
        else:
            print("enter valid answer")
options()

 
