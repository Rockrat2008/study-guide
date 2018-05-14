#  AUTHOR:  Michael O'Brien
#  CREATED:  11 May 2018
#  MODIFIED:  14 May 2018
#  DESCRIPTION:  Multiple Choice Study Quide


#  Import the random function to generate a random number for the guessing game
import random


#  Import the date and time module for the output to the text file scoring of the skit guessing game
from datetime import datetime

#  Variable Declaration
question = ' '
correctAnswer = ' '
wrongAnswer = ' '
feedback = ' '


#  Questions, answers, and feedback stored in a list of lists.
questions = ['What color is the sky', 'What barks', 'What meows', 'What color is grass']
wrongAnswers = ['red', 'cat', 'dog', 'purple']
correctAnswers = ['blue', 'dog', 'cat', 'green']
answerFeedback = ['The sky is blue because of refraction', 'Dogs bark because they are dogs', 'Cats meow because they are cats', 'Becaue of photosynthesis']
numberCorrect = 0
numberIncorrect = 0


def mainMenu():
    print()
    print('Welcome to my study guide')
    print()
    print('1 - Exam mode')
    print('2 - Study mode with feedback')
    print('3 - Exit')
    print()
    choice = input('Input the number to make your choice?  ')
    while len(choice) != 1:
        choice = input('Enter a single number between 1-3:  ')
    if int(choice) ==1:
        examMode(numberCorrect, numberIncorrect)
    elif int(choice) == 2:
        studyMode(numberCorrect, numberIncorrect)
    else:
        print('Thank you for using my study guide.')


def examMode(numberCorrect, numberIncorrect):
    userName = input('Enter your name to start exam mode:  ')
    while len(userName) < 1:
        userName = input('You need to enter your name to continue:  ')
    for question, wrongAnswer, correctAnswer in zip(questions, wrongAnswers, correctAnswers):
        print (question)
        randomize = random.randint(0,1)
        if randomize == 1:
            print ('A - ' + wrongAnswer)
            print ('B - ' + correctAnswer)
            print ()
            answer = getAnswer()
            if answer.upper() == 'A':
                numberIncorrect += 1
            elif answer.upper() == 'B':
                numberCorrect += 1
        else:
            print ('A - ' + correctAnswer)
            print ('B - ' + wrongAnswer)
            print()
            answer = getAnswer()
            if answer.upper() == 'A':
                numberCorrect += 1
            elif answer.upper() == 'B':
                numberIncorrect += 1
    print(userName + ' you got ' + str(numberCorrect) + ' right and ' + str(numberIncorrect) + ' wrong.')
        


def studyMode(numberCorrect, numberIncorrect):
    for question, wrongAnswer, correctAnswer, feedback in zip(questions, wrongAnswers, correctAnswers, answerFeedback):
        print (question)
        randomize = random.randint(0,1)
        if randomize == 1:
            print ('A - ' + wrongAnswer)
            print ('B - ' + correctAnswer)
            print ()
            answer = getAnswer()
            if answer.upper() == 'A':
                numberIncorrect += 1
            elif answer.upper() == 'B':
                numberCorrect += 1
        else:
            print ('A - ' + correctAnswer)
            print ('B - ' + wrongAnswer)
            print ()
            answer = getAnswer()
            if answer.upper() == 'A':
                numberCorrect += 1
            elif answer.upper() == 'B':
                numberIncorrect += 1
        print()
        print(feedback)
        input('Press enter for the next question')
        print()
    studyResults = print(userName + ' you got ' + str(numberCorrect) + ' right and ' + str(numberIncorrect) + ' wrong.')
    print(studyResults)


def getAnswer():
    testIsOver = False
    while not testIsOver:
        answer = input('Enter your answer:  ')
        answer = answer.upper()
        if len(answer) != 1:
            print('You must enter "A" or "B" as your answer:  ')
        elif answer not in "AB":
            print('You must enter "A" or "B" as your answer:  ')
        else:
            return answer


mainMenu()
