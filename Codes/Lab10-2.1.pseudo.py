#Imani Hollie 04.30.2024
#This program takes five test scores and calculates
#the average score and grade or displays an error message.

#Declare the main module [Inputs and Calls calcAverage()]
#1. Module main()
    #Declare local variables
    #a. Declare Float score1
    #b. Declare Float score2
    #c. Declare Float score3
    #d. Declare Float score4
    #e. Declare Float score5
    
    #Input for test scores
    #f. Display "Enter a test score: "
    #g. Input score1
    #h. Display "Enter a test score: "
    #i. Input score2
    #j. Display "Enter a test score: "
    #k. Input score3
    #l. Display "Enter a test score: "
    #m. Input score4
    #n. Display "Enter a test score: "
    #o. Input score5

    #Call the calcAverage module and pass score1, score2,
    #score3, score4, and score5 as reference
    #g. Call calcAverage(score1, score2, score3, score4,
                        #score5)
#1. End Module

#Output is then printed to the screen.

#Declare the calcAverage() module [Calculates, Outputs,
#and Calls determineGrade()]
#2. Module calcAverage(Float Ref score1, Float Ref score2,
                      #Float Ref score3, Float Ref score4,
                      #Float Ref score5,)

    #Declare variables
    #a. Declare Float avgScore
    #b. Declare Float s1
    #c. Declare Float s2
    #d. Declare Float s3
    #e. Declare Float s4
    #f. Declare Float s5
    
    #Calculate the average score
    #g. Set avgScore = (s1 + s2 + s3 + s4 + s5) / 5

    #Display the scores
    #h. Display "Test Score 1: ", s1
    #i. Display "Test Score 1: ", s1
    #j. Display "Test Score 1: ", s1
    #k. Display "Test Score 1: ", s1
    #l. Display "Test Score 1: ", s1
    #m. Display "Average Score: ", avgScore

    #Call the determineGrade module and pass avgScore as ref.
    #n. Call determineGrade(avgScore)
#2. End Module

#Declare the determineGrade module [Calculates and Outputs]
#3. Module mixColor(Float Ref grade)

    #Calculate the letter grade with an IF-THEN-ELSE decision structure
    #Display grade or error message

    #IF 100 >= grade and if grade >= 90 Display A
    #a. IF 100 >= grade >= 90 THEN
        #b. THEN Display "Grade: A"

        #ELSE IF 89 >= grade and if grade >= 80 Display B
        #c. ELIF 89 >= grade >= 80 THEN
            #d. THEN Display "Grade: B"

            #ELSE IF 79 >= grade and if grade >= 70 Display C
            #e. ELIF 79 >= grade >= 70 THEN
                #f. THEN Display "Grade: C"

                #ELSE IF 69 >= grade and if grade >= 60 Display D
                #g. ELIF 69 >= grade >= 60 THEN
                    #h. THEN Display "Grade: D"

                    #ELSE IF 59 >= grade Display F
                    #i. ELIF 59 >= grade THEN
                        #j. THEN Display "Grade: F"

                    #If argument passes through - display error message
                    #k. ELSE Display "ERROR! Vaild entries include digits."
                            #Display "Enter test scores again:"

                    #l. End If
                #m. End If
            #n. End If
        #o. End If
    #p. End If
#3. End Module