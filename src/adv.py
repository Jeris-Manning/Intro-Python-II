from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('adventurer', room['outside'])

# def holdUs():
#     room[player.room].describe()
#     print(player.room)
#     print(room[player.room].n_to)
#     player.room = room[player.room].n_to.name.lower()
#     print(player.room)
#     action = input("What would you like to do? Action: ")
#     print(action[0])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


# print(f'Welcome, brave {player.name}! May the good blood guide your way...')
# print("\n")

playing = True

exits = []

def handleRoom():
    global room
    print("\n")
    player.room.describe()
    global exits
    exits = []
    if hasattr(player.room, 'n_to'):
        exits.append([f"To the North lies a {player.room.n_to.name}.", "[n]orth", "n", player.room.n_to])
    if hasattr(player.room, 'e_to'):
        exits.append([f"To the East lies a {player.room.e_to.name}.", "[e]ast", "e", player.room.e_to])
    if hasattr(player.room, 's_to'):
        exits.append([f"To the South lies a {player.room.s_to.name}.", "[s]outh", "s",player.room.s_to])
    if hasattr(player.room, 'w_to'):
        exits.append([f"To the West lies a {player.room.w_to.name}.", "[w]est", "w", player.room.w_to])
    for cardinals in exits:
        print(cardinals[0])
    print("Press the bracketed key to move. Your options are: \n")
    for cardinals in exits:
        print(cardinals[1])
    print("[q]uit")

def handleMove():
    global playing
    global player
    global exits
    playerMove = input("Which way, adventurer?\n")
    formatMove = str(playerMove[0]).lower()
    for cardinals in exits:
        if formatMove == cardinals[2]:
            player.room = cardinals[3]
        elif formatMove == "q":
            playing = False
            quit()
        else:
            print("Not a good input")


    print("\n")




def adventureTime():

    while playing == True:
        handleRoom()
        handleMove()



# playerMove = input("What would you like to do?\n ")
    # print(playerMove)


adventureTime()
# print(room[player.room].name)


# for cardinals in room[player.room].roomExits():
#         print(room[player.room].n_to.name)
#         print(getattr(room[player.room], "name"))