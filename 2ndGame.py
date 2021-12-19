import random

print("Hello and Welcome to Kiko's Guessing Game!")

#Starting Point
_start_ = input("Do you want to play? ").lower()

if _start_ == 'yes':
    _max_number_ = input("Please pick a number that will serve as the highest number in this game. ")

    if _max_number_.isdigit():
        _max_number_ = int(_max_number_)

        #Random Number Picker
        _picked_number_ = random.randint(1, _max_number_)
    else:
        print("Are you dumb or something?!")
        quit()
else:
    print("See you next time!")
    quit()

print("If you ever want to quit the game just type the letter q.")
_user_guess_ = input("Now, please guess the number that has been randomly picked. ")

_number_of_guesses_ = 0

while True:

    if _user_guess_.isdigit():
        _user_guess_ = int(_user_guess_)
        if _user_guess_ == _picked_number_:
            print("Nice! You were able to guess the number")
            _number_of_guesses_ += 1
            break
        elif _user_guess_ < _picked_number_:
            print("Go Higher!")
            _number_of_guesses_ += 1
            _user_guess_ = input("Guess again.\n")
            continue
        else:
            print("Go Lower!")
            _number_of_guesses_ += 1
            _user_guess_ = input("Guess again.\n")
            continue
    elif _user_guess_ == 'q':
        print("See you next time!")
        quit()
    else:
        print("Really?!\nBye.")
        exit()

print("You took", _number_of_guesses_, "guesses")
print("Congratulations! I hope to see you next time!")
