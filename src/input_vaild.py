#This file for input vaildation

import getpass
from src.enc import Encrypt



# main class for input vaildation !
class Input_vaild:


    def __init__(self):


        self.stie_length = 30
        self.username_length = 20
        self.password_length = 50
        self.notes_length = 50
        self.e_obj = Encrypt()

        self.error_msg = lambda value, length: print(f"[!] {value} length is higher than {length} chars")
        self.length_error = lambda: print("[!] Password length Can't be less than  1 char")

        self.default_password_length = 30


    # site input
    def site_input(self):

        site = str(input("[+] Enter Site Name: ")).strip()

        while True:

            if len(site) > self.stie_length:
                self.error_msg("Site Name", self.stie_length)
                site = str(input("[+] Enter Site Name: ")).strip()


            else: return site; break


    # username input
    def username_input(self):

        username = str(input("[+] Enter Username: ")).strip()

        while True:

            if len(username) > self.username_length:

                self.error_msg("Username", self.username_length)
                username = str(input("[+] Enter Username: ")).strip()

            else: return username; break



    # get password choice from username y/n
    def password_choice(self):

        password_choice = str(input("[?] Do you want generate strong password? (y/n): ")).strip().lower()

        while True:

            if password_choice == "y": return "y"; break
            elif password_choice == "n": return "n"; break
            else: password_choice = str(input("[?] Do you want generate strong password? (y/n): ")).strip().lower()


    # ask user for password length input!
    def input_length(self):

        while True:

            try:

                password_length = int(input("[+] Enter Password length (Defalut 30): ") or self.default_password_length)
                
                if password_length > self.password_length:
                    self.error_msg("Password", self.password_length)
                    continue

                elif password_length < 1:
                    self.length_error()
                    continue


                #else: return password_length; break

            except ValueError:
                print(f"[!] Please Enter a vaild Number")
                #password_length = int(input("[+] Enter Password length (Defalut 30): ") or self.default_password_length)
                




            else: return password_length; break



    # password input
    def password_input(self):

        password_choice = self.password_choice()

        if password_choice == "y":

            password_length = self.input_length()
            
            password = self.e_obj.gen_strong_password(password_length); return password, password_choice
        

        elif password_choice == "n":

            password = str(getpass.getpass("[+] Enter Password: ")).strip()

            while True:

                if len(password) > self.password_length:
                    self.error_msg("Password", self.password_length)
                    password = str(getpass.getpass("[+] Enter Password: ")).strip()

                else: return password, password_choice; break


    # notes input
    def notes_input(self):

        notes = str(input("[+] Enter Notes (optinal): ") or "")
        
        while True:

            if len(notes) > self.notes_length:

                self.error_msg("Notes", self.notes_length)
                notes = str(input("[+] Enter Notes (optinal): ") or "")
            
            else: return notes; break



# test the code !
if __name__ == "__main__":

    i_obj = Input_vaild()


    site = i_obj.site_input()
    username = i_obj.username_input()
    password = i_obj.password_input()
    notes = i_obj.notes_input()


    print([site, username, password, notes])