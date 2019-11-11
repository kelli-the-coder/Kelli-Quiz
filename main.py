questions = []
def q1():
    while True:
        q = "What is Kelli's favorite video game currently?"
        print(q)
        print("a.Overwatch\nb.Minecraft\nc.Assassin's Creed\nd.Roblox")
        answer = input("Answer: ").lower()
        if answer == "a":
            questions.append(q)
            return answer
        elif answer == "b":
            questions.append(q)
            return answer
        elif answer == "c":
            questions.append(q)
            return answer
        elif answer == "d":
            questions.append(q)
            return answer
        else:
            print("That is not 'a', 'b', 'c', or 'd'!!")

def q2():
    while True:
        q = "What is Kelli's favorite food?"
        print(q)
        print("a.Salmon\nb.Strawberries\nc.Ribs \nd.Rice")
        answer = input("Answer: ").lower()
        if answer == "a":
            questions.append(q)
            return answer
        elif answer == "b":
            questions.append(q)
            return answer
        elif answer == "c":
            questions.append(q)
            return answer
        elif answer == "d":
            questions.append(q)
            return answer
        else:
            print("That is not 'a', 'b', 'c', or 'd'!!")

def q3():
    while True:
        q = "What is Kelli's mom's job at the school?"
        print(q)
        print("a.Lunch Lady\nb.Assistant Librarian\nc.Teaching Assistant\nd.Chinese Translater")
        answer = input("Answer: ").lower()
        if answer == "a":
            questions.append(q)
            return answer
        elif answer == "b":
            questions.append(q)
            return answer
        elif answer == "c":
            questions.append(q)
            return answer
        elif answer == "d":
            questions.append(q)
            return answer
        else:
            print("That is not 'a', 'b', 'c', or 'd'!!")

def q4():
    while True:
        q = "What is Kelli's all time favorite anime?"
        print(q)
        print("a.Attack on Titan\nb.Blue Exorcist\nc.One Piece\nd.Ouran High School Host Club")
        answer = input("Answer: ").lower()
        if answer == "a":
            questions.append(q)
            return answer
        elif answer == "b":
            questions.append(q)
            return answer
        elif answer == "c":
            questions.append(q)
            return answer
        elif answer == "d":
            questions.append(q)
            return answer
        else:
            print("That is not 'a', 'b', 'c', or 'd'!!")

def q5():
    while True:
        q = "What app does Kelli use most?"
        print(q)
        print("a.Instagram\nb.Discord\nc.Snapchat\nd.Twitter")
        answer = input("Answer: ").lower()
        if answer == "a":
            questions.append(q)
            return answer
        elif answer == "b":
            questions.append(q)
            return answer
        elif answer == "c":
            questions.append(q)
            return answer
        elif answer == "d":
            questions.append(q)
            return answer
        else:
            print("That is not 'a', 'b', 'c', or 'd'!!")

def q6():
    while True:
        q = "What is Kelli's favorite musical artist currently?"
        print(q)
        print("a.Ariana Grande\nb.Lil Pump\nc.Michael Jackson\nd.Juice Wrld")
        answer = input("Answer: ").lower()
        if answer == "a":
            questions.append(q)
            return answer
        elif answer == "b":
            questions.append(q)
            return answer
        elif answer == "c":
            questions.append(q)
            return answer
        elif answer == "d":
            questions.append(q)
            return answer
        else:
            print("That is not 'a', 'b', 'c', or 'd'!!")

def q7():
    while True:
        q = "Where was Kelli born?"
        print(q)
        print("a.Indiana\nb.China\nc.Illinois\nd.Florida")
        answer = input("Answer: ").lower()
        if answer == "a":
            questions.append(q)
            return answer
        elif answer == "b":
            questions.append(q)
            return answer
        elif answer == "c":
            questions.append(q)
            return answer
        elif answer == "d":
            questions.append(q)
            return answer
        else:
            print("That is not 'a', 'b', 'c', or 'd'!!")

def q8():
    while True:
        q = "What is Kelli's birthday?"
        print(q)
        print("a.March 17\nb.March 24\nc.March 8\nd.March 4")
        answer = input("Answer: ").lower()
        if answer == "a":
            questions.append(q)
            return answer
        elif answer == "b":
            questions.append(q)
            return answer
        elif answer == "c":
            questions.append(q)
            return answer
        elif answer == "d":
            questions.append(q)
            return answer
        else:
            print("That is not 'a', 'b', 'c', or 'd'!!")
def q9():
    while True:
        q = "What is Kelli's favorite sport?"
        print(q)
        print("a.Basketball\nb.Tennis\nc.Golf\nd.Football")
        answer = input("Answer: ").lower()
        if answer == "a":
            questions.append(q)
            return answer
        elif answer == "b":
            questions.append(q)
            return answer
        elif answer == "c":
            questions.append(q)
            return answer
        elif answer == "d":
            questions.append(q)
            return answer
        else:
            print("That is not 'a', 'b', 'c', or 'd'!!")
def q10():
    while True:
        q = "What language is Kelli taking?"
        print(q)
        print("a.Spanish\nb.French\nc.German\nd.Chinese")
        answer = input("Answer: ").lower()
        if answer == "a":
            questions.append(q)
            return answer
        elif answer == "b":
            questions.append(q)
            return answer
        elif answer == "c":
            questions.append(q)
            return answer
        elif answer == "d":
            questions.append(q)
            return answer
        else:
            print("That is not 'a', 'b', 'c', or 'd'!!")


print("How well do you know Kelli?? Well take this awesome quiz\
 to find out!")

while True:
    Go = input("Type 'start' to begin: ").lower()
    if Go == "start":
        break
    else:
        print("That isn't the word start!!")

while True:
    points = 0
    questions = []
    if q1() == "c":
        points += 1
        questions[0] += " Right, Assassin's Creed"
    else:
        questions[0] += " Wrong, correct answer was: Assassin's Creed"
    if q2() == "a":
        points += 1
        questions[1] += " Right, Salmon"
    else:
        questions[1] += " Wrong, correct answer was: Salmon"
    if q3() == "b":
        points += 1
        questions[2] += " Right, Assistant Librarian"
    else:
        questions[2] += " Wrong, correct answer was: Assistant Librarian"
    if q4() == "d":
        points += 1
        questions[3] += " Right, Ouran High School Host Club"
    else:
        questions[3] += " Wrong, correct answer was: Ouran High School Host Club"
    if q5() == "b":
        points += 1
        questions[4] += " Right, Discord"
    else:
        questions[4] += " Wrong, correct answer was: Discord"
    if q6() == "d":
        points += 1
        questions[5] += " Right, Juice Wrld"
    else:
        questions[5] += " Wrong, correct answer was: Juice Wrld"
    if q7() == "a":
        points += 1
        questions[6] += " Right, Indiana"
    else:
        questions[6] += " Wrong, correct answer was: Indiana"
    if q8() == "c":
        points += 1
        questions[7] += "Right, March 8"
    else:
        questions[7] += "Wrong, correct answer was: March 8"
    if q9() == "b":
        points += 1
        questions[8] += "Right, Tennis"
    else:
        questions[8] += "Wrong, correct answer was: Tennis"
    if q10() == "c":
        points += 1
        questions[9] += "Right, German"
    else:
        questions[9] += "Wrong, correct answer was: German"
    if points == len(questions):
        print("You got " + str(points) + "/" + str(len(questions)) + " points. Congratulations!! \
    \nShare your score with Kelli!")
    elif points >= len(questions) - 2:
        print("You got " + str(points) + "/" + str(len(questions)) + " points. Good job!! \
    \nShare your score with Kelli!")
    elif points >= len(questions) / 2:
        print("You got " + str(points) + "/" + str(len(questions)) + " points. Good Effort! \
        \nShare your score with Kelli!")
    elif points < len(questions) / 2 and points >= 2:
        print("You got " + str(points) + "/" + str(len(questions)) + " points. Big oof.. \
        \nShare your score with Kelli!")
    elif points < 2:
        print("You got " + str(points) + "/" + str(len(questions)) + " points. That's just sad bro.. \
        \nShare your score with Kelli!")

    while True:
        results = input("Do you want to see your results? (yes or no): ").lower()
        if results == "yes" or results == "no":
            break
        else:
            print("That is not 'yes or 'no'!!!!")

    if results == "yes":
        for i in range(len(questions)):
            print(questions[i])
    while True:
        rerun = input("Do you want to play again? (yes or no): ").lower()
        if rerun == "yes":
            again = False
            break
        elif rerun == "no":
            again = True
            break
        else:
            print("That is not 'yes' or 'no'!!!")
    if not again:
        continue
    else:
        break