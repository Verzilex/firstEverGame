import random

#StartingPage
_name_ = input("Please type your name: ").title()
_age_ = input("Please type your age: ")

if _age_.isdigit():
    _age_ = int(_age_)
    if _age_ < 18:
        _start_ = input("You sure you want to play, " + _name_ + "? ").lower()
        print("Well, no matter what you say, you will still play.\n:>")
    else:
        print(":>")
else:
    print("You're lucky.")

#1stPart
print(


_name_ + ": " +
'''
*mobile phone keyboard noises* 
What is this?
| Top 10 Horror Stories in the Philippines |
"10th - Once upon a time, there was a female student who attends her school life in the St. Thomas Aquinas Bldg. of UST Angelicum College
All of her classmates didn't like her very much because she acts weirdly infront of them.
This affected the way she had relationships with others if ever she had one.
She had a crush on one of the boys in her class.
However, since....."
Hmmm, no wonder the lowest is considered the lowest, the story is not even finished, although it kinda gives me goosebumps.
Oh no! I keep forgetting that I need to study, the first day of the 2nd quarter exams are tomorrow! ARGGHHHHH!


''')

choice_1 = input("""After sleeping, you heard your alarm go off. 
Subsequently, you get to decide what you are going to do.
Are you going to wake up now or sleep a bit more?
(Wake Up | Sleep More): """).lower()

if choice_1 == 'wake up': #WAKING UP
    print("""
    Narrator:
    After cramming for the exams tomorrow, you slept for the rest of the time and later you immediately woke up after hearing the alarm go off.
    Due to lack of sleep, you were pretty much out of your world but you atleast had time to eat breakfast.
    Since you woke up early, you were also able to take your time in going to school, so you packed the things that you needed for school.
    When you got near the proximity of the school, you saw a girl looking out a window from the building that you will be entering, but you ignored it.
    As you entered the school grounds, you saw you're friends and joined them in going to your own respective classrooms.
    """)

    backpack = ['pens', 'notes', 'water jug', ['crayons', 'scissors', 'ruler'], 'phone', 'wallet']

    choice_2a = input("""After entering the classroom, you still got time left before the exams.
    So, you get to decide what you are going to do.
    Are you going to review while waiting or sleep for a bit to compensate waking up early a while ago.
    (Review | Sleep): """).lower()

    if choice_2a == 'review': #REVIEWING
        print("""
        Narrator:
        You decided to review, so you tried to find your notes in your backpack.
        *zipping sound*
        In your backpack, there were multiple things including:""", backpack[0] + ",", backpack[1] + ",", backpack[2] + ",", backpack[3][0] + ",", backpack[3][1] + ",", backpack[3][2] + ",", backpack[4] + ",", backpack[5])
        
        while True:
            op_backpack = input("Choose something from the backpack: ").lower()
            if op_backpack == 'notes':
                print("You got your notes and began reviewing")
                break
            elif op_backpack == 'phone':
                print("You got your phone and saw what you searched last night.\nYou remembered the story and got distrubed alot.")
                break
            elif op_backpack in backpack or op_backpack in backpack[3]:
                print("What you chose is useless for reviewing; please choose another item.")
                continue
            else:
                print("What you chose is not in your backpack; please choose the items that are available in your backpack.")
                continue
        
        print("""
        Narrator:
        As you got your item, you got a glimpse of someone outside the corridor.
        
        """
        + _name_ + ':'
        """
        Who is that?
        A student?
        Why is he outside?
        Students are not allowed to go outside of their classrooms in this kind of time.
        W...Wait a minute.
        *looks away from the boy*
        *looks back*
        *looks away again*
        Oh my god! WHY IS HE LOOKING AT ME!
        Ok, ok, just focus on your tests 
        """ + _name_ + "." 
        """
        Maybe, I'm just seeing things because I wasn't able to sleep properly.
        """)

    else: #NAPPING
        print("""
        Narrator:
        You decided to take a nap before taking the quiz.
        As you took a nap, you were dreaming of having fun while being with your friends in school.
        As you were having fun, you noticed someone at the back staring at your group.
        It wasn't clear but you had a hunch that it was a boy and the same age with you and your friends.
        You came closer to find out, but as you approached...
        You were woken up by one of your friends in your class because it was time to take the exam.
        """)

    print("""
    Narrator:
    It was already 4:30 P.M. when the last examination finished.
    After the examinations, your friends asked you if you wanted to join them playing for a bit.
    """)

else: #SLEEP
    print("""
    Narrator:
    After sleeping a bit more, you luckily woke up and saw the time.
    You realized that you were almost late, so you need to rush to go to school.
    In doing so, you weren't able eat breakfast and pack everything up.
    As you hurried up going to school and get into your specific assigned classroom, you realized that you weren't able to bring a pen for the exam that you will be taking.
    """)

    choice_2b = input("""After you realizing that you didn't bring a pen, you get to decide what you are going to do.
    Are you going to borrow a pen from your classmate or go to the bookstore near the canteen?
    (Borrow | Buy): """).lower()

    if choice_2b == 'borrow': #BORROWING
        pass
    else: #BUYING
        pass






















Orig_Book = open("article.txt", "w")
Orig_Book.write('''
Once upon a time, there was a female student who attends her school life in the St. Thomas Building.
All of her classmates didn't like her very much because she acts weirdly infront of them.
This affected the way she had relationships with others if ever she had one.
She had a crush on one of the boys in her class.
However, since she was known and seen as a weird girl, even her crush rejected her.
Because of the situation that she had, she got depressed and soon can't take it anymore, so she decided to kill her crush and herself after.
Some people say that this story is fake but,
some of the others also say that she haunts the place because she harnessed hatred and jealousy for the people that can develop a good relationship with others smoothly."
''')
Orig_Book.close()

def Reading_Orig_Book ():
    Orig_Book = open("article.txt", "r")
    print(Orig_Book.read())
    Orig_Book.close()


