# Importing modules
import random as r
import sys
import sqlite3 as s
import time
from collections import deque 



# To save the user name of the user so they can access their data later
user_name = str(input("Please input your user name: "))

# A class for my database so it is all in one place
class db():
    def __init__(self):
        #To set up the database
        self.conn = s.connect("Users results, history and passwords.db")
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute("""CREATE TABLE user_data (
                                name TEXT, 
                                password TEXT, 
                                balance INTEGER
                                )""")
        except s.OperationalError:
            pass
        self.conn.commit()

    
    # A function to inser data if the user has a new account
    def insert_userdata(self, username):
        with self.conn:
            self.cursor.execute("INSERT INTO user_data VALUES (?, ?, ?)", (username, mode.passw, mode.balance))

    # A function to set the user balance from the database when the user wants to see it
    def get_userbalance(self,username):
            with self.conn:
                self.cursor.execute("SELECT * FROM user_data WHERE name = ?", (username,))
                return self.cursor.fetchone()[2]
    
    # A fucntion to get the password of the user and compare it to the value written
    def get_userpass(self,username):
            with self.conn:
                self.cursor.execute("SELECT * FROM user_data WHERE name = ?", (username,))
                return self.cursor.fetchone()[1]
    
    # A function to update the balance of the user if the user gets or loses money
    def update_balance(self, username):
        with self.conn:
            self.cursor.execute("""UPDATE user_data SET balance = ? WHERE name = ?""",(mode.balance, username))
    
    # A function to see if the user account exists or not, if it doesn't it will raise an error so i used an exception
    def check_existence_account(self, username):
        with self.conn:
            self.cursor.execute("SELECT * FROM user_data WHERE name = ?", (username,))
            try:
                self.username_to_check = type(self.cursor.fetchone()[0])
                if self.username_to_check == str:
                    mode.enter_pass()
                else:
                    pass

            except TypeError:
                mode.new_pass()


class mode_setup:

    def __init__(self):
        # The variable used to store the user's balance left
        self.balance = 100

        
        # The variables i am using for the prototype password
        self.passw_tries = 0
        
        #setting up the queue
        self.queue = deque([""])
    # To make the user input their new password
    def new_pass(self):
        self.passw_user = str(input("We haven't detected your account, please input a password to create your account." 
                                    " Note you will start with the 100£ you inputed, enter your password here: "))
        self.passw = self.passw_user
        dbase.insert_userdata(user_name)
        self.passw_check = str(input(f"Welcome {user_name} please input your password: "))
        
        # To make sure the password is correct and to repeat it a max of 3 times if it is incorrect, if they failed it exits the program
        while self.passw_check != self.passw and  self.passw_tries < 3:
            self.passw_check = str(input("Incorrect password, please Input the password to your account again: "))
            self.passw_tries += 1
        
        if self.passw_tries >= 3:
            print("Incorrect passowrd, please contact the casino to reset your password")
            time.sleep(20)
            sys.exit()
    
    #To make the user input their old password
    def enter_pass(self):
        self.passw = str(dbase.get_userpass(user_name))
        self.passw_check = str(input(f"Welcome {user_name} please input your password: "))
        
        # To make sure the password is correct and to repeat it a max of 3 times if it is incorrect, if they failed it exits the program
        while self.passw_check != self.passw and  self.passw_tries < 3:
            self.passw_check = str(input("Incorrect password, please Input the password to your account again: "))
            self.passw_tries += 1
        
        if self.passw_tries >= 3:
            print("Incorrect passowrd, please contact the casino to reset your password")
            time.sleep(20)
            sys.exit()
    
        
    # A Function for the mode chose to help make the game work till the user quits or his money ends
    def chosen_mode(self):
    
    # To choose which mode to play according to the player's answer
        if mode.mode_chosen == 1:
            mode.first_approach()
        elif mode.mode_chosen == 2:
            mode.second_approach()
        elif mode.mode_chosen == 3:
            mode.third_approach()
        else:
            pass
    
    
    
    
    # A function to print the disclaimer and to see if the player want to play or view balance
    def game_or_balance(self):
        self.disclaimer_play_or_not = int(input("DISCLAIMER, you must agree that you are more than likely to lose your money and that the odds are against you."
                                               " Do you want to play the game or view your balance? Choose 1 to play game, 2 to see your win/lose history or any other number to view balance and exit: "))

    
    # A function to see which mode the player chose and to make it easier to make the user change the mode later in game
    def play_or_not(self):
        
        if self.disclaimer_play_or_not == 1:
            # To see which mode the player wants to play   
            self.mode_chosen = int(input("Do you want to play with High risk, Medium risk mode 1 or  Medium risk mode 2? Choose 1 if high, 2 if medium mode 1, 3 if medium mode 2: "))
            
            while self.mode_chosen != 1 and self.mode_chosen != 2 and self.mode_chosen != 3:
                self.mode_chosen = int(input("Please input either 1 for High risk, 2 for medium mode 1, 3 for medium mode 2: "))
        
        elif self.disclaimer_play_or_not == 2:
            print(self.queue)
           
        
        else:
            print(f"Your balance is: {dbase.get_userbalance(user_name)}") 
            print("Thank you for playing")
            time.sleep(20)
            sys.exit()
    
    
    
    # A function that lay the foundation of the first way to play the game of chance(high risk)
    def first_approach(self):

        # An infinite loop to make the game run till the balance is zero or the user want to stop
        while True:
            self.play = int(input("Do you want to start in first mode? choose 1 to start and 2 to stop: "))
            computer_bet = r.randint(0,36)
            
            # To check if the user chose to play or now
            if self.play == 1 and self.balance > 0:
                # The variable used to store the number that the user inputs
                self.bet = int(input("Enter the number you want to place a bet on: "))
                self.balance -= 10
                dbase.update_balance(user_name)
                
                # A while loop to make sure that the user only inputs numbers between 0 and 36
                while self.bet < 0 or self.bet > 36:
                    self.bet = int(input("Please input a number between 0 and 36: "))
                
                # To see if the user bet is the same as the random number generated 
                if self.bet == computer_bet:
                    self.balance += 360
                    dbase.update_balance(user_name)
                    print(f"Congrats you won! your balance now is {dbase.get_userbalance(user_name)}")
                    self.queue.append("Won")
                else:
                    print(f"You lost, your balance now is {dbase.get_userbalance(user_name)}")
                    self.queue.append("Lost")
            
                # To check if the balance is zero and if that is the case it it doesn't proceed
            elif self.balance <= 0:
                top_up = int(input("No balance left, do you want to top up or close the game? choose 1 to top up or any other number to close the game: "))
                if top_up == 1:
                    self.balance += 100
                    dbase.update_balance(user_name)
                    break
                else:
                    print("No balance left, please top up and come back")
                    time.sleep(20)
                    sys.exit()
            
            else:
                print(f"Your balance is: {dbase.get_userbalance(user_name)}")
                break
        


    # A function that lay the foundation of the second way to play the game of chance(medium risk)
    def second_approach(self):

        
        # An infinite loop to make the game run till the balance is zero or the user want to stop
        while True:
            self.play = int(input("Do you want to start in second mode? choose 1 to start and 2 to stop: "))
            computer_bet = (r.randint(0,36))%2
            
            # To check if the user chose to play or now
            if self.play == 1 and self.balance > 0:
                # The variable used to store the number that the user inputs
                self.bet = int(input("Enter the type of number you want to place a bet on, choose 1 if even and 2 if odd: "))
                self.balance -= 10
                dbase.update_balance(user_name)
                
                # To make sure the number inputted is either zero or one
                while self.bet != 1 and self.bet != 2:
                    self.bet = int(input("Please input either 1 for even or zero for odd: "))

                # To see if the user bet is the same as the random number generated 
                if self.bet == 1 and computer_bet == 0:
                    self.balance += 20
                    dbase.update_balance(user_name)
                    print(f"Congrats you won! your balance now is {dbase.get_userbalance(user_name)}")
                    self.queue.append("Won")
            
                else:
                    print(f"You lost, your balance now is {dbase.get_userbalance(user_name)}")
                    self.queue.append("Lost")
            
            # To check if the balance is zero and if that is the case it it doesn't proceed
            elif self.balance <= 0:
                top_up = int(input("No balance left, do you want to top up or close the game? choose 1 to top up or any other number to close the game: "))
                if top_up == 1:
                    self.balance += 100
                    dbase.update_balance(user_name)
                    break
                else:
                    print("No balance left, please top up and come back")
                    time.sleep(20)
                    sys.exit()
            
            else:
                print(f"Your balance is: {dbase.get_userbalance(user_name)}")
                break
    
    
    # A function that lay the foundation of the thirs way to play the game of chance(medium risk)
    def third_approach(self):

        
        # An infinite loop to make the game run till the balance is zero or the user want to stop
        while True:
            self.play = int(input("Do you want to start in third mode? choose 1 to start and 2 to stop: "))
            computer_bet = r.randint(0,36)
            if computer_bet > 0 and computer_bet < 19:
                computer_bet = 1
            else:
                computer_bet = 2
            
            # To check if the user chose to play or now
            if self.play == 1 and self.balance > 0:
                
                # The variable used to store the number that the user inputs
                self.bet = int(input("Enter the range of numbers you want to place the bet on, choose 1 if from 1 to 19 and 2 if from 20 to 36: "))
                self.balance -= 10
                dbase.update_balance(user_name)
                
                # To make sure the number inputted is either zero or one
                while self.bet != 1 and self.bet != 2:
                    self.bet = int(input("Please input either 1 if the range is from 1 to 19 or 2 if the range is from 20 to 36: "))

                # To see if the user bet is the same as the random number generated 
                if self.bet == computer_bet:
                    self.balance += 20
                    dbase.update_balance(user_name)
                    print(f"Congrats you won! your balance now is {dbase.get_userbalance(user_name)}")
                    self.queue.append("Won")
            
                else:
                    print(f"You lost, your balance now is {dbase.get_userbalance(user_name)}")
                    self.queue.append("Lost")
            
            # To check if the balance is zero and if that is the case it it doesn't proceed
            elif self.balance <= 0:
                top_up = int(input("No balance left, do you want to top up or close the game? choose 1 to top up or any other number to close the game: "))
                if top_up == 1:
                    self.balance += 100
                    dbase.update_balance(user_name)
                    break
                else:
                    print("No balance left, please top up and come back")
                    time.sleep(20)
                    sys.exit()
            
            else:
                print(f"Your balance is: {dbase.get_userbalance(user_name)}")
                break

mode = mode_setup()
dbase = db()

dbase.check_existence_account(user_name)
mode.game_or_balance()
while True:
    mode.play_or_not()
    try:
        mode.chosen_mode()
    except AttributeError:
        pass
    mode.disclaimer_play_or_not = int(input("Do you want to play the game or view your balance? Choose 1 to play game, 2 to see your win/lose history or any other number to view balance and exit: "))

