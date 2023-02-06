def main() -> None:
    """Entrypoint of program."""
    global points
    greet()
    points = 0
    again: bool = False
    while not again:
        print("You have the option to either \"quit\" this simulation or play one of the two following games: \"rockpaperscissors\" or \"murdermystery\". ")
        game_type: str = input("In the following line, please choose which path you would like to take: ")
        if game_type == str("rockpaperscissors"):
            rock_paper_scissors()
        elif game_type == str("murdermystery"):
            points = mystery(points)
        elif game_type == str("quit"):
            sad: str = "\U0001F972"
            print(f"Sorry to see you leave {sad}.")
            again = True
        print(f"You currently have a total of {points} points.")


def greet() -> None:
    """Welcome message."""
    global player
    player = input("What is your name? ")
    print(f"Welcome, {player}!")
        

def rock_paper_scissors() -> None:
    """Rock, paper, scissors game."""
    global points
    global player
    from random import randint
    opponent: int = randint(1, 3)
    SAD: str = "\U0001F972"
    SMILE: str = "\U0001F604"
    print(f"Welcome, {player} to Rock, Paper, Scissors! ")
    print("You will have the option to choose from the following: rock, paper, or scissors.")
    print("Rock beats scissors, scissors beats paper, and paper beats rock. Choose wisely.")
    you: str = input("\"rock\", \"paper\", or \"scissors\"? ")
    # rock: int = 1
    # scissors: int = 2
    # paper: int = 3
    if you == str("rock"):
        if opponent == 1:
            points += 2
            print(f"You chose rock. The opponent chose rock. Tie! You earned 2 points! {SMILE}")
        if opponent == 2:
            points += 5
            print(f"You chose rock. The opponent chose scissors. You beat the opponent! You earned 5 points {SMILE}!")
        if opponent == 3:
            print(f"You chose rock. The opponent chose paper. You lose. You earned no points {SAD}.")
    if you == str("scissors"):
        if opponent == 1:
            print(f"You chose scissors. The opponent chose rock. You lose. You earned no points {SAD}.")
        if opponent == 2:
            points += 2
            print(f"You chose scissors. The opponent chose scissors. Tie! You earned 2 points! {SMILE}")
        if opponent == 3:
            points += 5
            print(f"You chose scissors. The opponent chose paper. You beat the opponent! You earned 5 points {SMILE}!")
    if you == str("paper"):
        if opponent == 1:
            points += 5
            print(f"You chose paper. The opponent chose rock. You beat the opponent! You earned 5 points! {SMILE}")
        if opponent == 2:
            print(f"You chose paper. The opponent chose scissors. You lose. You earned no points {SAD}.")
        if opponent == 3:
            points += 2
            print(f"You chose paper. The opponent chose paper. Tie! You earned 2 points! {SMILE}")
    

def mystery(total_points: int) -> int:
    """Murder mystery game."""
    global player
    print(f"Welcome {player} to Murder Mystery!")
    print("Your job as the detective is to find who killed Mr. Red with what weapon.")
    print("There are 3 weapons that you suspect Mr. Red may have been killed by: knife, rope, poison.")
    MRS_RED: str = "\U0001F9D3"
    MS_GREEN: str = "\U0001F469"
    MR_GREY: str = "\U0001F468"
    print(f"There are 3 people who you suspect that may have killed Mr. Red: Mrs. Red {MRS_RED}, Ms. Green {MS_GREEN}, Mr. Grey {MR_GREY}.")
    print("You only get 2 tries and 4 hints to figure out who killed Mr. Red and what he was killed with.")
    print("However, each hint except the first hint given will take away 2 points from the initial 20 points.")
    print("You will only be able to ask for hints one time in the game, so choose very wisely.")
    print("You enter Mr. Red's bedroom where he is found dead on the floor. In his hand is a knife. On his nightstand is an empty cup. Under his bed is a rope.")
    hints: int = 0
    total_points += 20
    end: bool = False
    while not end and hints < 4:
        given_hint: str = input("Would you like a hint? ")
        if given_hint == str("yes"):
            if hints == 0:
                hints += 1
                print("The murderer does not have a beard.")
            elif hints == 1:
                total_points -= 2
                hints += 1
                print("The murder weapon is not sharp.")
            elif hints == 2:
                total_points -= 2
                hints += 1
                print("The murderer was a close friend of Mr. Red.")
            elif hints == 3:
                total_points -= 2
                hints += 1
                print("The murder weapon did not cause any external harm to Mr. Red.")
        if given_hint == str("no") or hints >= 4:    
            guess: str = input("Who is the murderer and what is the murder weapon? Please type it in this format: ms./mr./mrs. name, weapon. ")
            if guess == str("ms. green, poison"):
                print(f"You caught the murderer and the murder weapon! Congratulations! You've earned a total of {total_points} points!")
                end = True
            else:
                guess_two: str = input("Sorry, but that was incorrect. One last try. Who is the murderer and what is the murder weapon? Please type in the same format as before. ")
                if guess_two == str("ms. green, poison"):
                    print(f"You caught the murderer and the murder weapon! Congratulations! You've earned a total of {total_points} points!")
                    end = True
                else:
                    print(f"The murderer was not caught! Try again next time! You've earned a total of {total_points}.")
                    end = True
    return total_points   


points: int
player: str
game_type: str = ""
if __name__ == "__main__":
    main()
rde