#  AUTHOR:  Michael O'Brien
#  CREATED:  11 May 2018
#  MODIFIED:  15 May 2018
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
displayResults = ' '
numberCorrect = 0
numberIncorrect = 0


#  Questions, answers, and feedback variables
questions = ['What color is the sky', 'What barks', 'What meows', 'What color is grass']
wrongAnswers = ['red', 'cat', 'dog', 'purple']
correctAnswers = ['blue', 'dog', 'cat', 'green']
answerFeedback = ['The sky is blue because of refraction', 'Dogs bark because they are dogs', 'Cats meow because they are cats', 'Becaue of photosynthesis']


#  Main menu function to allow user to choose exam mode, study mode, and to view previous results.
def mainMenu():
    print()
    print('Welcome to my study guide')
    print()
    print('1 - Exam mode')
    print('2 - Study mode with feedback')
    print('3 - View previous exam mode results')
    print('4 - View previous study mode results')
    print('5 - Exit')
    print()
    choice = input('Input the number to make your choice?  ')
    while len(choice) != 1:
        choice = input('Enter a single number between 1-5:  ')
    if int(choice) ==1:
        examMode(numberCorrect, numberIncorrect)
    elif int(choice) == 2:
        studyMode(numberCorrect, numberIncorrect)
    elif int(choice) == 3:
        viewResults('examModeResults.txt')
    elif int(choice) == 4:
        viewResults('studyModeResults.txt')
    else:
        print('Thank you for using my study guide.')


#  Exam mode function tests the user without the ability to provide feedback and stores the results in a file
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
    testScore = numberCorrect/(numberCorrect+numberIncorrect)*100
    testResults = userName + ' you got ' + str(numberCorrect) + ' right and ' + str(numberIncorrect) + ' wrong.  Your score is:  ' + str(testScore) + '%.'
    print(testResults)
    saveResults('examModeResults.txt', testResults)
        

#  Study mode function tests the users knowledgte and provides feedback on missed questions.  Results are stored in a file
def studyMode(numberCorrect, numberIncorrect):
    userName = input('Enter your name to start study guide mode:  ')
    while len(userName) < 1:
        userName = input('You need to enter your name to continue:  ')
    for question, wrongAnswer, correctAnswer, feedback in zip(questions, wrongAnswers, correctAnswers, answerFeedback):
        print (question)
        randomize = random.randint(0,1)
        if randomize == 1:
            print ('A - ' + wrongAnswer)
            print ('B - ' + correctAnswer)
            print ()
            answer = getAnswer()
            if answer == 'A':
                numberIncorrect += 1
                print(feedback)
            elif answer == 'B':
                numberCorrect += 1
        else:
            print ('A - ' + correctAnswer)
            print ('B - ' + wrongAnswer)
            print ()
            answer = getAnswer()
            if answer == 'A':
                numberCorrect += 1
            elif answer == 'B':
                numberIncorrect += 1
                print(feedback)
        print()
        input('Press enter for the next question')
        print()
    testScore = numberCorrect/(numberCorrect+numberIncorrect)*100
    studyResults = userName + ' you got ' + str(numberCorrect) + ' right and ' + str(numberIncorrect) + ' wrong.  Your score is:  ' +str(testScore) + '%.'
    print(studyResults)
    saveResults('studyModeResults.txt', studyResults)


#  The get answer function is called from both exam and study mode and validates the users answer to confirm it is only a valid choice
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


#  This module allows the user to view the previous results in either exam or study mode
def viewResults(resultsFile):
    results = open(resultsFile, 'r')
    displayRsults = results.read()
    print()
    print(displayRsults)
    results.close()
    mainMenu()
    

#  This function saves the user results to a file
def saveResults(resultsFile, scores):
    dateTested = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    results = open(resultsFile, 'a')
    results.write(dateTested + '\n')
    results.write(scores + '\n')
    results.write('\n')
    results.close()
    input ('Press enter to return to the main menu.')
    mainMenu()


mainMenu()
