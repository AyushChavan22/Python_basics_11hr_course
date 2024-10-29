# ROCK, PAPER, SCISSOR GAME
print("WELCOME TO ROCK PAPER SCISSOR GAME!!! FIRST GAME OF AYUSH!!")
o=input("Enter your name to play:- ")
def r_p_s(n):
    for n in range(1,n+1):
        import random
        computer = random.choice([1,2,3])
        youstr =input("Enter your choice:- ")
        youdict = {"rock": 1, "paper": 2, "scissor": 3}
        reverseyoudict= {1:"rock", 2:"paper", 3: "scissor" }
        you = youdict[youstr]
        print(f"You chose {reverseyoudict[you]}\nComputer chose {reverseyoudict[computer]}")
        if(computer==you):
            print("Oops! It's a draw!")
        else:
            if(computer==1 and you==2):
                print("YOU WIN!!!")
            elif(computer==1 and you==3):
                print("YOU LOSE!!!, TRY AGAIN!!")
            elif(computer==2 and you==1):
                print("YOU LOSE!!!, TRY AGAIN!!")
            elif(computer==2 and you==3):
                print("YOU WIN!!!")
            elif(computer==3 and you==1):
                print("YOU WIN!!!")
            elif(computer==3 and you==2):
                print("YOU LOSE!!!, TRY AGAIN!!")
            else:
                print("Something went wrong!")
r_p_s(3)
print(f"Thank youh for playing, {o}!!!")
    