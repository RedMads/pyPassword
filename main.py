"""
Hi guys im RedMad :$, today i made this password manager!

offline, secure, locally password manager !


special Thanks to:

    @wzxmpl <3


concat us:

    email: RedMads@protonmail.com
    github: https://github.com/RedMads/

- RedMad :$
"""

from src.manage_db import DB
from src.enc import Encrypt
from src.banner import Banner
import os



class Main:

    def __init__(self):
        
        self.db_obj = DB()
        self.e_obj = Encrypt()

        self.clear = lambda: os.system("clear") # clear function !

    def welcome(self):

        with open("resources/welcome.txt", "r") as file:

            print(file.read()); file.close()



    def main(self):
        
        try:
            self.db_obj.create_master_tb()
            self.db_obj.create_data_tb()
        except: pass
        

        if not self.db_obj.check_if_hash_exists():
            
            self.welcome()

            print("\n\n")
            input("Press Any Key to continue... ")

            self.clear(); Banner()

            self.db_obj.get_masster_password()
            self.db_obj.create_data_tb()
            print("[$] Sign Up Done, Try login!")



        else:
            self.db_obj.master_login()



if __name__ == "__main__":

    m_obj = Main()

    m_obj.clear()

    Banner()

    m_obj.main()



        