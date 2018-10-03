import recipes

done = False
print("Welcome to grocery helper!")
print("To see a list of commands type 'help'\nTo exit grocery helper type 'quit'")

while(not done):
    response = input("What would you like to do? ")
    resp = response.split()
    switch (resp[0].lower()):
        case "h" or "help":
            print("--------------------")
            print("List of commands:")
            print("'help': prints out the help menu")
            print("'add items': opens item adder where you can add individual items to your list")
            print("'add recipes': opens recipe adder where you can add recipes to your list")
            print("'quit': exits grocery helper")
            print("--------------------")
            break
        
