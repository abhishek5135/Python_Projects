import time
import random
def turn(num):
    player_1=0
    player_2=0
    listcomputer=['snake','water','gun']
    computer=random.choice(listcomputer)
    num2=0
    while(num2!=num):

        print("snake","water","gun")
        players_inpu = input("Player 1 Enter your choice from above ")
        print(f"computer choice {computer}")
        if(computer=='snake' and players_inpu=='water'):
            player_2+=1
        elif (computer=='gun' and players_inpu=='water'):
            player_1+=1
        elif(computer=='water' and players_inpu=='water'):
            print("Turn draw")

        elif(computer=='gun' and players_inpu=='snake'):
            player_2+=1
        elif (computer=='water' and players_inpu=='snake'):
            player_1+=1
        elif(computer=='snake' and players_inpu=='snake'):
            print("Turn draw")

        elif(computer=='snake' and players_inpu=='gun'):
            player_1+=1
        elif (computer=='water' and players_inpu=='gun'):
            player_2+=1
        elif(computer=='gun' and players_inpu=='gun'):
            print("Turn draw")
        num2+=1    

    if(player_1>player_2):
        print("You are winner of This game ")
    elif (player_2>player_1):
        print("You lose the game")    
        print("Better luck next time")

if __name__ == "__main__":
    start=time.time()
    num3=int(input("Enter how Turns you want to play "))
    turn(num3)
    end=time.time()
    print(f"Runtime of the program is {end - start}")

    