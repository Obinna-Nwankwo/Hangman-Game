import random




WORD_LIST  =  ["obim", "nwankwo", "official", "obyi"]

CHOSEN_WORD  =  random.choice(WORD_LIST)


LIVE  =  6




DISPLAY  =  []
for leter in range(len(CHOSEN_WORD)):
    DISPLAY  += "_"


end  =  False

while not end:
    print("\n\n--------------------------------------------------\n")
    GUESS  =  input("Please make a guess \n:").lower()
    print("\n--------------------------------------------------\n")

    if GUESS not in CHOSEN_WORD:
        LIVE -= 1
   
    print(f"Mind you guess cus you have, {LIVE} remianing")
    print("\n--------------------------------------------------\n")

    if LIVE == 0:
        print("\n--------------------------------------------------\n")
        print("You lose")
        print("\n--------------------------------------------------\n")
        break

    for position in range(len(CHOSEN_WORD)):
        letter  =  CHOSEN_WORD[position]
        if letter == GUESS:
            DISPLAY[position]  = letter

    
    print(DISPLAY)

    if "_" not in DISPLAY:
        end = True
        print("\n--------------------------------------------------\n")
        print("You Won")
        print("\n--------------------------------------------------\n")