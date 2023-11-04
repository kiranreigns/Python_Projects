import time
import os
from colored import fg # import this module to print colored text on terminal
from HarryPotter import hogwards,acromantulas,magic_object # import this module to display text art

# colors
red = fg('red')
yellow =fg('yellow')
green =fg('green')
magenta = fg('magenta')
blue = fg('blue')
cyan =fg('cyan')
white = fg('white')
black = fg('black')

# here goes the intro
def intro():
    print(white+"WELCOME TO HOGWARDS!🏰") # text color + text to be printed on terminal
    time.sleep(2)
    print(white + hogwards)
    print(green + "You are a student at Hogwarts School of Witchcraft and Wizardry. ")
    time.sleep(2)
    print("You have been dared to explore the Forbidden Forest.")
    time.sleep(2)
    print("Your goal is to find and retrieve a rare magical object hidden deep within the forest.")
    time.sleep(2)
    print(black + magic_object)
    print(red + "Be cautious, for danger lurks in every shadow.")

def quit():  # this function clears the terminal
    os.system('cls')

def forbidden_forest():
    print(blue + "\nYou enter the Forbidden Forest and are immediately surrounded by darkness.")
    time.sleep(2)
    print("You hear rustling in the bushes nearby.")
    time.sleep(2)
    print("Do you want to use a Lumos 🪄  spell to light your wand or proceed in the dark?")

    choice = input("Enter 'Lumos' / 'proceed' / 'quit': ").lower()

    if choice == 'quit': # clears the terminal when user enters quit
        quit()
        return 

    elif choice == "lumos":
        print(magenta +"\nYour wand illuminates the path ahead.")
        time.sleep(2)
        print("You encounter a group of Acromantulas. They are drawn to the light.")
        time.sleep(2)
        print(black + acromantulas)
        print(cyan +"Do you want to run, try to calm them, or send a signal for help?")

        acromantula_choice = input("Enter 'run' / 'calm' / 'signal' / 'quit': ").lower()

        if acromantula_choice == "run":
            print(red +"\nYou escape the Acromantulas, but you've lost your way in the forest. Game Over!")

        elif acromantula_choice == "quit":
            quit()
            return

        elif acromantula_choice == "calm":
            print(yellow +"\nYou manage to calm the Acromantulas and they lead you to a clearing.")
            time.sleep(2)
            print("Your friends, Hermione and Ron, appear to help you.")
            time.sleep(2)
            print("Together, you find the hidden object. Congratulations, you win!")

        elif acromantula_choice == "signal":
            print(red +"\nYou send up sparks with your wand, signaling for help.")
            time.sleep(2)
            print("However, the signal attracts a group of Death Eaters.")
            time.sleep(2)
            print("Do you want to fight or flee?")

            death_eater_choice = input("Enter 'fight' / 'flee' / 'quit': ").lower()
        
            if death_eater_choice == "fight":
                print(yellow +"\nYour friends have come to rescue you. You all engage in a fierce battle and emerge victorious.")
                time.sleep(2)
                print("You find the hidden object 🧹. Congratulations, you win!")

            elif death_eater_choice == "flee":
                print(red +"\nYou manage to escape, but the Death Eaters seize the hidden object. Game Over!")

            elif death_eater_choice == "quit":
                quit()
                return

            else:
                print(white +"Invalid choice. Please try again.")
                forbidden_forest()
        else:
            print(white +"Invalid choice. Please try again.")
            forbidden_forest()

    elif choice == "proceed":
        print(cyan +"\nYou proceed cautiously but trip over a root and make noise.")
        time.sleep(2)
        print("A group of sinister Dementors appears. They feed on your fear.")
        time.sleep(2)
        print("Do you want to cast a Patronus charm, seek help, or succumb to fear?")
        dementor_choice = input("Enter 'Patronus' / 'help' / 'succumb' / 'quit': ").lower()

        if dementor_choice == "patronus":
            print(yellow +"\nYour Patronus ..🦌.. repels the Dementors. You continue your journey.")
            time.sleep(2)
            print("You find the hidden object 🧹. Congratulations, you win!")

        elif dementor_choice == "help":
            print(green +"\nYour calls for help summon Hagrid, who drives away the Dementors.")
            time.sleep(2)
            print("You find the hidden object 🧹 with Hagrid's guidance. Congratulations, you win!")

        elif dementor_choice == "succumb":
            print(red +"\nThe Dementors consume your happiness. You are left in despair. Game Over!")

        elif dementor_choice =="quit":
            quit()
            return

        else:
            print(white +"Invalid choice. Please try again.") # this will be printed incase user enters an invalid choice
            forbidden_forest()
    else:
        print(white +"Invalid choice. Please try again.")
        forbidden_forest()

if __name__ == "__main__":
    intro()
    forbidden_forest()
   
