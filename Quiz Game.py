print("Welcome to Ruth's quiz!")
playing= input("Do you want to play? ")
if playing.lower() != "yes" :
    quit()
print ("Okay! Let's play :).")
score = 0
q1 = input ("what does element 'O' represents on the periodic table? ")
if q1.lower() == "oxygen":
    print ("Correct!")
    score +=1
else :
    print ('Incorrect!')
q1 = input ("what is the the name of the river that runs through Egypt? ")
if q1.lower() == "nile":
    print ("Correct!")
    score +=1
else :
    print ('Incorrect!')
q1 = input ("what is the capital of russia? ")
if q1.lower() == "moscow":
    print ("Correct!")
    score +=1
else :
    print ('Incorrect!')
q1 = input ("how many letters are in the word 'hippopotamus'? ")
if q1.lower() == "12":
    print ("Correct!")
    score +=1
else :
    print ('Incorrect!')
q1 = input ("how many days are in a leap year? ")
if q1.lower() == "366":
    print ("Correct!")
    score +=1
else :
    print ('Incorrect!')

print ("You got " + str(score) + " questions correctly!")
print ("You got "+ str((score/5)*100) + " %.")