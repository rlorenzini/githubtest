#rock paper scissors
#rock>scissors>paper>rock
print("\nLET THE STRONGEST SURVIVE!!!\n")
user1 = ""
user2 = ""

print("\nPress q to Quit. ")


def winner():
    if user1 == "rock":
        if user2 == "rock":
            print("\nTIE.\n")
        elif user2 == "paper":
            print("\nPLAYER TWO WINS.\n")
        elif user2 == "scissors":
            print("\nPLAYER ONE WINS.\n")
    if user1 == "paper":
        if user2 == "rock":
            print("\nPLAYER ONE WINS.\n")
        if user2 == "paper":
            print("\nTIE.\n")
        if user2 == "scissors":
            print("\nPLAYER TWO WINS.\n")
    if user1 == "scissors":
        if user2 == "rock":
            print("\nPLAYER TWO WINS.\n")
        if user2 == "paper":
            print("\nPLAYER ONE WINS.\n")
        if user2 == "scissors":
            print("\nTIE.\n")
def quit():
    if user1 == "q":
        print("\nThanks for playing!")
while user1 != "q":
    user1 = input("\nPlayer One: Rock/Paper/Scissors::\n").lower()
    user2 = input("\nPlayer Two: Rock/Paper/Scissors::\n").lower()
    winner()
else:
    quit()
