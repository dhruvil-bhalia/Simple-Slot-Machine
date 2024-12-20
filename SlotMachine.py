# SIMPLE_SLOT_MACHINE

import random

def slot_machine():
    symbols = ["!!!!", "@@@@", "$$$$", "&&&&", "****"]
    
    while True:
        tokens = int(input("Enter the number of tokens you want to play with: "))
        if tokens <= 0:
            print("You must enter a positive number of tokens.")
            continue

        while tokens > 0:
            print(f"You have {tokens} tokens.")
            bet = int(input("Enter your bet amount: "))

            if bet > tokens:
                print("You don't have enough tokens for that bet.")
                continue
            elif bet <= 0:
                print("Your bet must be a positive number.")
                continue

            tokens -= bet

            reel1 = random.choice(symbols)
            reel2 = random.choice(symbols)
            reel3 = random.choice(symbols)

            print("\n----- SLOT MACHINE -----")
            print(f"| {reel1} | {reel2} | {reel3} |")
            print("-----------------------\n")

            if reel1 == reel2 == reel3:
                winnings = bet * 3
                tokens += winnings
                print(f"JACKPOT! You won {winnings} tokens!")
            else:
                print("Better luck next time!")

        print("You've run out of tokens. Game over.")
        break

if __name__ == "__main__":
    slot_machine()
    