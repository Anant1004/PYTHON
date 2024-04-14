
def printboard(xstate, zstate):
    print(f"1 | 2 | 3")
    print(f"--|---|---")
    print(f"1 | 2 | 3")
    print(f"--|---|---")
    print(f"1 | 2 | 3")




if __name__ == "__main__":
    xstate = [0,0,0,0,0,0,0,0]
    zstate = [0,0,0,0,0,0,0,0]
    turn = 1
    print("Welcome to Tic-Tac-Toe game")
    
    while (True):
        printboard(xstate,zstate)
        if (turn == 1):
            print("1st player chance")
            value = int(input("Enter you choice"))
            xstate[value] = 1 
        else:
            print("2nd player chance")
            value = int(input("Enter your choice"))
            xstate[value] = 1 

        break