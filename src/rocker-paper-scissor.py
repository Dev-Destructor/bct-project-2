import random

# Rock Paper Scissor Game
def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None;

    # Check for all possibilities when computer chose s
    elif comp == 'r':
        if you=='p':
            return False;
        elif you=='s':
            return True;
        else:
          print('Invalid Input! You have not entered r, p or s, try again!')
          return exit()
    
    # Check for all possibilities when computer chose w
    elif comp == 'p':
        if you=='s':
            return False;
        elif you=='r':
            return True;
        else:
          print('Invalid Input! You have not entered r, p or s, try again!')
          return exit()
    
    # Check for all possibilities when computer chose g
    elif comp == 's':
        if you=='r':
            return False;
        elif you=='p':
            return True;
        else:
          print('Invalid Input! You have not entered r, p or s, try again!')
          return exit()

print("Comp Turn: Rock(r) Paper(p) or Scissor(s)? ");
randNo = random.randint(1, 3);
if randNo == 1:
    comp = 'r';
elif randNo == 2:
    comp = 'p';
elif randNo == 3:
    comp = 's';

you = input("Your Turn: Rock(r) Paper(p) or Scissor(s)? ");
a = gameWin(comp, you);

print(f"Computer chose {comp}");
print(f"You chose {you}");

if a == None:
    print("The game is a tie!");
elif a:
    print("You Win!");
else:
    print("You Lose!");
