#author: Gianni M. Javier
# Assignment: For Loops: Basic I

# Objectives:
# Learn how to use basic for loop statements in Python
# Practice some basic algorithms in Python
# Create a Python file called for_loop_basic1.py that performs the following tasks.

print() #Prints a new line

# Basic - Print all integers from 0 to 150.

for integer in range(151): #Runs the for loop from range 0 to 150 and assigns the value to the variable integer for each iteration
    print(integer) #Prints the value of the variable integer for each iteration of the for loop
print() #Prints a new line after the completion of the for loop

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000

for multiples in range(5,1001,5): #Runs the for loop from range 5 to 1000 in increments of 5 and assigns the value to the variable multiples for each iteration
    print(multiples) #Prints the value of the variable multiples for each iteration of the for loop
print() #Prints a new line after the completion of the for loop

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

for integer in range(1,101): #Runs loop from 1 to 100 and assigns the value to the variable integer for each iteration
    if integer % 5 == 0: # If statement with Condition, which evaluates whether the integer divided by 5 results in a remainder equal to 0
        print('Coding') #Prints the String 'Coding if the condition of the If statement is met to be True
    if integer % 10 == 0: #If statement with Condition, which evaluates whether the integer divided by 10 results in a remainder equal to 0
        print('Coding Dojo') #Prints the String 'Coding Doojo' if the condition of the If statement is to me to be True
    if integer % 5 != 0 and integer % 10 != 0: #If statement with Condition, which evaluates whether the integer divided by 5 and 10 results in a remainder not equal to 0
        print(integer) #Prints the value of the variable integer if the condition the If statement is met to be True
print() #Prints a new line after the completion of the for loop

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

sumOfOddIntegers = 0 #initializes the variable sumOfOddIntegers in order to begin the process of storing and adding the sum of odd integers
for oddInteger in range(500001): #Runs loop from 0 to 500,000 and assigns the value to the variable oddInteger for each iteration
    if oddInteger % 2 != 0: #If statement with Condition, which evaluates whether the value of the variable oddInteger is not even
        sumOfOddIntegers += oddInteger #Processes the addition of the value of the variable oddInteger to the value of the variable sumOfOddIntegers for every iteration of the for loop where the condition of the If statement is met to be True
print(sumOfOddIntegers) #Prints the value of the variable sumOfOddIntegers
print() #Prints a new line after the completion of the for loop

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for countDownByFours in range(2018,-1,-4): #Runs the loop from 2018 to 0 in incements of 4 and assigns the value to the variable countDownByFours for each iteration
    print(countDownByFours) #Prints the value of the variable countDownByFours for every iteration of the loop
print() #Prints a new line after the completion of the for loop

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. 
# For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = int(input('Please input a low number: ')) #Asks the user to input a low number and sets the value to the variable lowNum
highNum = int(input('Please input a high number: ')) #Asks the user to input a high number and sets the value to the variable highNum
mult = int(input('Please input a multiple: ')) #Asks the user to input a multiple and sets the value to the variable mult

for flexibleCounter in range(lowNum,highNum + 1): #Runs the for loop starting from the value of the variable lowNum to the value of the variable highNum and assigns the value to the variable flexibleCounter for each iteration
    if flexibleCounter % mult == 0: #If statement with Condition, which checks if the value of the variable flexibleCounter divided by the value of the variable mult has a remainer equal to 0
        print(flexibleCounter) #Prints the value of the variable flexibleCounter if the Condition of the If statement is met to be True