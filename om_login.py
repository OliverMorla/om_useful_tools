# simple login/register system using python where data is stored locally.
import os

class database: # Class
    def __init__(self): 
        self.close_program = True
        print("Welcome!")
        
    def login_menu(self):
        print("0: Exit")
        print("1: Register")
        print("2: Login")
        while self.close_program:
            try:
                myChoice = int(input("Enter a number: "))
            except:
                os.system('cls')
                self.login_menu() 
                
            if(myChoice == 0):
                self.close_program = False
                print("Thank you for using Oliver's Registration System")
                exit()
            elif(myChoice == 1):
                self.register()
            elif(myChoice == 2):
                self.login()

    def register(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        file_register = open(username + ".txt", "a")
        file_register.writelines([username + "\n", password])
        file_register.close()

    def login(self):
        username = input("Enter your username: ")
        if (os.path.exists(username + ".txt")):
            file_open = open(username + ".txt", "r")
            for line in file_open:
                if(line == username + "\n"):
                    print("Found user")
                    password = input("Enter your password: ")
                    for line in file_open:
                        if(line == password):
                            print("You are now signed in")
                            self.close_program = False
                        else:
                            print("Enter the correct password") 
        else:
            print("Username does not exist try again!")