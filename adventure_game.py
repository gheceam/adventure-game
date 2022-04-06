import random
import time

lands = ['Narnia', 'Asgard', 'Elysian Fields', 'Troy', 'Crete', 'Dacia']
locations = ['Baldur\'s Castle 🏰', 'Gold Mountain 🏔',
             'Sacred Volcano 🌋 of Asgororth', 'Palimira\'s Fountain ⛲️']
treasures = ['Hope Diamond 💎', 'Joser\'s Crown 👑',
             'Dragon Ring 💍', 'Golden Bell 🔔']
have_pebble = False


def print_pause(message, interval=1):
    print(message)
    time.sleep(interval)


def reset_game():
    global have_pebble
    have_pebble = False


def intro():
    land = random.choice(lands)
    location = random.choice(locations)
    treasure = random.choice(treasures)
    print_pause(f"\nYou are traveling across {land} seeking a {treasure}")
    print_pause(f"You are standing on the banks of The River {land} 🌊")
    print_pause(
        f"To get the treasure you must cross the river and get to {location}")


def suspense(interval):
    for i in range(interval):
        print_pause(".", .5)


def get_pebble():
    global have_pebble

    choice = valid_input("""
Just then you see a clear blue pebble by the water.
Do you pick it up?
Enter 1 to pickup up the pebble.
Enter 2 to not pickup pebble.""", ['1', '2'])

    if choice == '1':
        have_pebble = True
        print_pause("\nYou pick up the pebble and put it in your pocket.")
    elif choice == '2':
        have_pebble = False
        print_pause(
            "\nYou kick the pebble away. It will only weigh you down.")


def swim():
    print_pause("You dive into the river and start swimming.")
    print_pause("Half way across you are exhausted and start to sink down.", 2)

    suspense(5)

    if have_pebble:
        print_pause(
            "\nAll of a sudden underwater the blue pebble starts to glow.")
        suspense(3)
        print_pause("The magic pebble let's you breathe underwater.")
        print_pause("\n!!!!Congraulations!!!!")
        print_pause("\nYou made it to the other side and got the treasure!")
        print_pause("\n\nGAME OVER")
    else:
        print_pause("\nSadly you don't make it across.")
        print_pause("You swallowed too much river.\n\nGAME OVER")


def walk():
    print_pause("\nYou walk for what seems like eternity and find no bridge.")

    choice = valid_input("""
Do you dare to swim across or keep walking?
Enter 1 to swim across the river.
Enter 2 to walk and find a way across.""", ['1', '2'])

    if choice == '1':
        swim()
    elif choice == '2':
        print_pause("You drop dead tired and exhausted.\n")
        print_pause(
            "Seems you've reached the end of the road for this adventure.")
        print_pause("The treasure will never be yours.\n\nGAME OVER")


def valid_input(prompt, options):
    string = f"""What would you like to do?
(Please enter {options[0]} or {options[1]}): """

    choice = input(f"{prompt} {string}")
    if choice in options:
        return choice
    else:
        print_pause('Please make a choice.')
        return valid_input(prompt, options)


def swim_or_walk():
    string = """\nYou will have to either walk along the river
to find a bridge, or swim across.
Enter 1 to swim across the river.
Enter 2 to walk and find a way across."""

    choice = valid_input(string, ['1', '2'])
    get_pebble()

    if choice == '1':
        swim()
    elif choice == '2':
        walk()


def play_again():

    string = """\nWould you like to play again?
Enter 'y' to play again.
Enter 'n' to end this adventure."""

    choice = valid_input(string, ['y', 'n'])

    if choice == 'y':
        reset_game()
        start()
    elif choice == 'n':
        print_pause("\nThank you for playing adventurer! Goodbye!")


def start():
    intro()
    swim_or_walk()
    play_again()


start()
