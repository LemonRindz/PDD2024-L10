#Imani Hollie 04.30.2024
#This program takes five test scores and calculates
#the average score and grade or displays an error message.

#Module 1 - main() [Calls getScores(), calcAverage() and determineGrade() and Outputs]

#Modularize the scores for simplification and cleaner code
#Module 2 - getScores() [Inputs and Outputs]
def getScores():
    #Inputs----------------------------------------------------------------------------------------
    #This is the same as repeating 'score1 = float(input('Enter Test Score 1: '))' five times
    #This uses a for loop with a range of 5 and a counter ({num + 1}) to count/stop the loop, or:
    #for num in range(5):
        #score = float(input(f'Enter Test Score {num + 1}: '))
        #scores.append(score)
    scores = [float(input(f'Enter Test Score {num + 1}: ')) for num in range(5)]
    #Output----------------------------------------------------------------------------------------
    return scores
#End Module 2

#Module 3 - caclAverage() [Calculates and Outputs]
#Instead of having test scores and averages printed here, just calculate the scores
def calcAverage(scores):
    #Calculations----------------------------------------------------------------------------------
    #The sum function literally add all of the inputs
    avgScore = sum(scores) / 5
    #Output----------------------------------------------------------------------------------------
    return avgScore
#End Module 3

#Module 4 - determineGrade() [Calculates and Outputs]
def determineGrade(avgScore):
    #Calculations----------------------------------------------------------------------------------
    #IF-THEN-ELSE decision structure will display letter grade or an error message if false
    #IF 100 >= grade >= 90 THEN Display A
    if 100 >= avgScore >= 90:
        #This is the same as repeating 'print('Final Grade: #')'
        return 'A'
    #ELSE IF 89 >= grade >= 80 THEN Display B
    elif 89 >= avgScore >= 80:
        return 'B'
    #ELSE IF 79 >= grade >= 70 THEN Display C
    elif 79 >= avgScore >= 70:
        return 'C'
    #ELSE IF 69 >= grade >= 60 THEN Display D
    elif 69 >= avgScore >= 60:
        return 'D'
    #ELSE IF 59 >= grade >= 0 THEN Display F
    elif 59 >= avgScore >= 0:
        return 'F'
    #If argument passes through - display error message
    else:
        return 'ERROR! Valid entries include digits with 2 decimal places'
    #End If
#End Module 4

#Call Modules and Declare Variables----------------------------------------------------------------
scores = getScores()
avgScore = calcAverage(scores)
grade = determineGrade(avgScore)
#Outputs-------------------------------------------------------------------------------------------
#This is the same as repeating 'print(f'Test Score 1: {s1}')' five times
print(f'Test Scores: {scores}')
print(f'Average Test Score: {avgScore:.2f}')
print(f'Final Grade: {grade}')

#End Module 1