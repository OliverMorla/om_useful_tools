import os
import math
import random

from om_login import database

def useful_tools_menu(): # Menu
    print("Welcome to om_useful_tools v0.1")

    myList = {
        0: "0: Exit",
        1: "1: Calculator",
        2: "2: Mad Libs",
        3: "3: Guessing Game",
        4: "4: Array Sorter"
    }
    
    i = 0
    while i < len(myList):
        print(myList.get(i))
        i += 1
    
    choice = int(input("Enter a number: "))
    if(choice == 0):
        exit()
    elif(choice == 1):
        calculator()
    elif(choice == 2):
        mad_libs()
    elif(choice == 3):
        guessing_game()
    elif(choice == 4):
        array_sorter()
    elif(choice == 5):
        array_sorter()
        
def calculator(): #om_calculator is a basic calculator with basic arithmetic operators.
    print("Welcome to om_calculator v0.1")

    print("Input -1 to go back to menu for op")
    num1 = float(input("Enter the first number: "))
    op = str(input("Enter a operator (+, -, /, x, %, -1): "))
    num2 = float(input("Enter the second number: "))

    if(op == '+'):
        result = num1 + num2
        print(result)
    elif(op == '-'):
        result = num1 - num2
        print(result)
    elif(op == 'x'):
        result = num1 * num2
        print(result)
    elif(op == '/'):
        result = num1 / num2
        print(result)
    elif(op == '%'):
        result = num1 % num2
        print(result)
    elif(op == '-1'):
        os.system('cls')
        useful_tools_menu()

def mad_libs():# Mad libs Game
    print("Welcome to om_mad_libs v0.1")

    verb_1 = input("Enter a verb of choice: ")
    adj_1 = input("Enter a adjective of choice: ")
    verb_2 = input("Enter second verb of choice: ")
    body_part = input("Enter a body part name of choice: ")
    adverb = input("Enter an adverb of choice: ")
    body_part_2 = input("Enter any body name of your choice: ")
    noun = input("Enter a noun of choice: ")
    verb_3 = input("Enter the third verb of choice: ")
    animal = input("Enter name of any animal of choice: ")
    noun_2 = input("Enter an noun of choice: ")
    verb_4 = input("Enter the fourth verb of choice: ")
    adj_2 = input("Enter an adjective of chioce: ")
    color = input("Enter any color name: ")

    story = "Most doctors agree that bicycle of" + verb_1 + " is a/an " + adj_1 + " form of exercise." + verb_2 +" a bicycle enables you to develop your " + body_part + " muscles as well as " + adverb + " increase the rate of a " + body_part_2+" beat. More " + noun + " around the world "+ verb_3 +" bicycles than drive "+ animal +". No matter what kind of "+ noun_2 +"you "+ verb_4 +", always be sure to wear a/an "+ adj_2 +" helmet.Make sure to have  " + color + " reflectors too! "

    print(story)

def guessing_game(): # This function creates a guessing game based on the range of numbers inputted. User will have tries to guess the randomly generated number between the given range.
    print("Welcome to om_guessing_game v0.1")

    # Taking Inputs
    lower = int(input("Starting Number: "))
    
    # Taking Inputs
    upper = int(input("Ending Number: "))
    
    # generating random number between
    # the lower and upper
    x = random.randint(lower, upper)
    print("\n\tYou've only ",
        round(math.log(upper - lower + 1, 2)),
        " chances to guess the integer!\n")
    
    # Initializing the number of guesses
    count = 0
    
    # for calculation of minimum number of
    # guesses depends upon range
    while count < math.log(upper - lower + 1, 2):
        count += 1
    
        # taking guessing number as input
        guess = int(input("Guess a number: "))
    
        # Condition testing
        if x == guess:
            print("Congratulations you did it in ",
                count, " try")
            # Once guessed, loop will break
            break
        elif x > guess:
            print("You guessed too small!")
        elif x < guess:
            print("You Guessed too high!")
    
    # If Guessing is more than required guesses,
    # shows this output.
    if count >= math.log(upper - lower + 1, 2):
        print("\nThe number is %d" % x)
        print("\tBetter Luck Next time!")

def array_sorter(): # This function takes in an unsorted array of inputs and sorts them using insertion sort algorithm.
    print("Welcome to om_array_sorter v0.1")

    # creating an empty list
    arr = []
    
    # number of elements as input
    n = int(input("Enter number of elements : "))
    
    # iterating till the range
    for k in range(0, n):
        el = int(input())
    
        arr.append(el) # adding the element
    
    # Iterating through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    print(arr)


 
database_object = database()
database_object.login_menu()

os.system('cls')
useful_tools_menu()
