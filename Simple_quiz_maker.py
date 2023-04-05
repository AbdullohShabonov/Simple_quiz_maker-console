# Simple quizz maker

import random

# Creating variables
questions_multiple = []
fake_answers = []

questions_typeAnswer = []

grade = 0

continuous_app = True


# First function that asks from user to select an operation type or Exit, and
#                                                 return another function respectively as type written by user
def quest_adding():
    global continuous_app

    print("""M -  Multiple Choice
T  -  Type the answer
0 - Exit""")

    type = input("Please select the Quizz type:   T/M  => ").lower()
    if type == 'm':
        return multiple_choice()
    elif type == 't':
        return type_answer()
    elif type == '0':
        continuous_app = False
        return 0
    else:
        print("Please input T or M letters only !")
        return quest_adding()


# Creating function that collect only Type-the-Answer quiz elements into questions_typeAnswer[] list
def type_answer():
    quest = input("Input the question: ")
    answer = input("Correct answer: ")
    questions_typeAnswer.append([quest, answer])
    print("\n")

    # Asking from user to continue to add question or stop
    cont = input("Do you want to add a question?     Y/N  :\n").lower()
    if cont == 'y':
        return quest_adding()
    else:
        return quest_releasing()


# Another function that collect only Multiple-Choice quiz elements into questions_multiple[], fake_answer[] lists
def multiple_choice():
    quest = input("Input the question: ")
    answer = input("Correct answer: ")
    questions_multiple.append([quest, answer])
    fake_answer = input("Input 3 wrong answers: ").split(',')
    while len(fake_answer) != 3:
        print("Sorry you can only add 3 wrong answers (with separation of ',' )!")
        fake_answer = input("Input 3 wrong answers: ").split(',')
    fake_answers.append(fake_answer)
    print("\n")

    # Asking from user to continue to add questions or stop
    cont = input("Do you want to add a question?     Y/N  :\n").lower()
    if cont == 'y':
        return quest_adding()
    else:
        return quest_releasing()


# Final function that release all saved questions as a Test
def quest_releasing():
    quest_number = 1
    grade_X = 0

    if questions_typeAnswer:
        for quest, answer in questions_typeAnswer:
            print(f"""
{quest_number} - question:
   {quest}""")
            user_answer = input("""   aswer :=> """).lower()
            if user_answer == answer.lower():
                print("Congratulations correct answer !")
                grade_X += 1
            else:
                print("Sorry wrong answer !")
            quest_number += 1

    if questions_multiple:
        index = 0
        # Collecting all answers from fake_answers[] list and questions_multiple[correct_answer_multiple]
        #                                                               and randomizing the order of the answers
        for quest, answer in questions_multiple:
            all_answers = [answer] + [i for i in fake_answers[index]]
            random.shuffle(all_answers)

            # Creating a, b, c, d key with shuffled order
            dict = {'a': all_answers[0].strip(' .'), 'b': all_answers[1].strip(' .'),
                    'c': all_answers[2].strip(' .'), 'd': all_answers[3].strip(' .')}

            # Printing the ready multiple-choice test
            print(f"""{quest_number}- question:
   {quest}""")

            # print(f"""a) {list(dict.values())[0]}\nb) {all_answers[1]}\nc) {all_answers[2]}\nd) {all_answers[3]}""")

            for i in range(len(dict)):
                print(f"{list(dict.keys())[i - 1]}) {list(dict.values())[i - 1]}")

            # Grading system: 1. Asking from the user their answer
            #                 2. Checking if user-answer the same as with correct answer
            #                 3. Giving a feedback respectively with the result of the user-answer checking
            user_answer = input("""   answer :=> """).lower()
            while not user_answer in dict.keys():
                print("Please choose one of the keys (a, b, c, d) !")
                user_answer = input("""   javob :=> """).lower()
            if list(dict.keys()).index(user_answer.lower()) == list(dict.values()).index(answer):
                print("Congratulations correct answer !")
                grade_X += 1
            else:
                print("Sorry wrong answer !")
            quest_number += 1
            index += 1

    # Printing the score with counting correct answers
    print(f"""\n
    Good job !
    Your score is {grade + grade_X} from {quest_number - 1} ! """)
    print("\n")

    return 0

# Making the application work without stopping until user pressed 0 to Exit
while continuous_app:
    print('\n')
    quest_adding()
