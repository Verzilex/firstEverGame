print("Welcome to Kiko's Kiddy Game!")

#Starting Point
_start_ = input("Do you want to try playing Kiko's Kiddy Game?\nYes or No: ")

if _start_ != ("Yes"):
    exit()

print("""Before we start playing, please answer the following questions first to proceed to Kiko's Kiddy Game.
Please answer properly and honestly because it can affect the game that you will be playing""")
_name_ = input("What is your name? ")
_age_1_ = int(input("How old are you? "))
print("Initiating sequence of ...\ngameplay questions.")

#1st Question
_answer_ = input("First Question! Is Kiko handsome?\nYes or No: ")

if _answer_ != ("Yes"):
    print("You suck.")
    _answer_ = input("For another time, is Kiko handsome?\nYes or No: ")
    if _answer_ != ("No"):
        print("Ok, I forgive you for the mistake that you did.")
    else:
        print("You have a bad taste!\nYou don't deserve to play this game!")
        exit()
else:
    print("Stop it! You're making me blush.")

#2nd Question
_answer_ = input("What do you think is better, UST Main or USTAC? " )

if _answer_ == ("UST Main"):
    print("Hmmmm, okay not a bad choice.")
    _answer_ = int(input("From 1 - 10, How much are you enjoying your school life right now? "))
    if _answer_ <= (6):
        print("I hope you're doing fine and enjoy more of your time there!")
    elif _answer_ <= (10):
        print("School just hits different bro.")
    else:
        print("I h%ve w4rN3d Y&o")
        print("Oops, something might have gone wrong. Oh well, back to the questions.")
elif _answer_ == ("USTAC"):
    print("I knew it, the OG is still the best one!")
    _answer_ = int(input("I remember so many memories being there.\nRate your time being there from 1 - 10. "))
    if _answer_ <= (6):
        print("I hope you're doing fine and enjoy more of your time there!")
    elif _answer_ <= (10):
        print("School just hits different bro.")
    else:
        print("W3 h%ve w4rN3d Y&o")
        print("Oops, something might have gone wrong. Oh well, back to the questions.")
else:
    print("What do you think you are doing?\nYou shouldn't do that, I'm warning you!")
    _answer_ = input("Anyways, how have you been?\nHave you been enjoying your time lately?\nYes or No: ")
    if _answer_ == ("Yes"):
        print("Nice! If you ever have a problem just ask for help from me.")
    elif _answer_ == ("No"):
        print("Aww, I hope you get to enjoy your time while taking this game.")
    else:
        print("W3 h%ve w4rN3d Y&o")
        print("Oops, something might have gone wrong. Oh well, back to the questions.")

#3rd Question
_age_2_ = int(input("Just to really make sure, how old are you? "))

if _age_1_ == (_age_2_):
    print("Okay, listen here, you've got to esc4p3 n0W o# 1t wIll b2 T0o LATE!")
    print("You're safe as long as you leave now.")
    print("""DO
    YOU
    THINK
    YOU
    CAN
    ESCAPE
    ME, """ + _name_ + "!?")
    exit()
else:
    print("oh NO! w3 H4v3 wARn3D YOU!\nYoU sH0U1d hAVE 1Ist3N3D!")
    _exit_trial_input_ = input("""Exit the game NOW!!!
Do you want to exit the game?
___ or No: """)
    if _exit_trial_input_ != ("apiwnfawobfia"):
        print("Th!$ G4mE iS CuR$3D!")
        print("$Hut DOWN y0uR COMPUTER AND DON'T EVER PLAY THIS GAME ANYMORE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("N0 MaTT3R whAt yOu D0, Don'T eV34 l00K B3H1Nd YoU!!!")
        print("........")
        print(".......")
        print("......")
        print(".....")
        print("....")
        print("...")
        print("..")
        print(".")
        print("")
        print(":)")
        exit()
