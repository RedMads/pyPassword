#This File for manage the database get, insert data in database

from src.enc import Encrypt
from src.input_vaild import Input_vaild
from src.banner import Banner
from src.check_os import Check_os
import sqlite3, getpass, bcrypt, os, prettytable, sys, json


# Database Class
class DB:

    def __init__(self):

        self.db_name = "db/database.db"
        self.conn = sqlite3.connect(self.db_name)
        self.c = self.conn.cursor()
        self.clear = lambda: os.system("clear") # clear function !

        self.len_salt = 30

        try:
            self.create_master_tb = lambda: self.c.execute("CREATE TABLE master(password TEXT, salt TEXT);")
            self.insert_master = lambda vlaue: self.c.execute(f'INSERT INTO master(password, salt) VALUES("{str(vlaue.decode())}","{str(self.e_obj.generator(self.len_salt))}");'); self.conn.commit()

        except:

            pass

        self.rounds = 14
        self.prefix = b"2a"

        self.aes_key = None
        self.old_aes_key = None
        self.dflt_pass = 30

        self.e_obj = Encrypt()
        self.i_obj = Input_vaild()
        self.os_obj = Check_os()

        self.table = prettytable.PrettyTable()
        self.salt = self.get_salt()

        self.new_salt = self.e_obj.generator(self.len_salt)

        
    # Create the data table in the database
    def create_data_tb(self):

        try:
            self.c.execute("""CREATE TABLE data(
                                    site text,
                                    username text,
                                    password text,
                                    notes text
                        );""")

        except:

            pass





    # insert encrypted data into data table
    def insert_into_data(self, site, username, password, notes=""):

        self.c.execute(f"""INSERT INTO data(
                                site,
                                username,
                                password,
                                notes
                      ) VALUES(
                          '{site}',
                          '{username}',
                          '{password}',
                          '{notes}'
                      );""")

        self.conn.commit()


    # get all data from the data table
    def get_all_data(self):

        
        sites = self.c.execute("SELECT site FROM data;").fetchall()
        usernames = self.c.execute("SELECT username FROM data;").fetchall()
        passwords = self.c.execute("SELECT password FROM data;").fetchall()
        notes = self.c.execute("SELECT notes FROM data;").fetchall()


        return (
            sites,
            usernames,
            passwords,
            notes
        )



    # decrypt all encrypted data and store it in arrays!
    def dec_all_data(self, key):

        sites, usernames, passwords, notes = self.get_all_data()

        enc_sites = []
        enc_usernames = []
        enc_passwords = []
        enc_notes = []

        Id = []

        for i in range(len(sites) + 1):
            
            Id.append(i)

        Id.remove(0)
        
        for site in sites:

            enc_sites.append(site[0])

        decrypted_sites = self.e_obj.decrypt(enc_sites, key)

        for username in usernames:

            enc_usernames.append(username[0])

        decrypted_usernames = self.e_obj.decrypt(enc_usernames, key)

        for password in passwords:

            enc_passwords.append(password[0])

        decrypted_passwords = self.e_obj.decrypt(enc_passwords, key)

        for note in notes:

            enc_notes.append(note[0])

        decrypted_notes = self.e_obj.decrypt(enc_notes, key)


        return (
            decrypted_sites,
            decrypted_usernames,
            decrypted_passwords,
            decrypted_notes,
            Id
        )


    # encrypted all data !
    def enc_all_data(self, key):

        (
            sites, usernames,
            passwords, notes, Id
        ) = self.dec_all_data(key)

        enc_data = []
        

        for i in range(len(sites)):

            encrypted_data = self.e_obj.encrypt([
                sites[i], usernames[i], 
                passwords[i], notes[i]
            ], key)

            enc_data.append(encrypted_data)

        return enc_data




    # decrypt all data and sort it [site, username, password, note]
    def dec(self, key):

        enc_data = self.enc_all_data(key)

        dec_data = []

        for data in enc_data:

            decrypted_data = self.e_obj.decrypt(data, key)
            dec_data.append(decrypted_data)


        return dec_data



    # list all decrypted data in table
    def list_linux(self):

        self.table.clear(); print("\n")

        (
            sites, usernames,
            passwords, notes, Id
        ) = self.dec_all_data(self.aes_key)

        self.table.add_column("id", Id)
        self.table.add_column("site", sites)
        self.table.add_column("username", usernames)
        self.table.add_column("password", passwords)
        self.table.add_column("note", notes)

        print(self.table); print("\n")



    # this function list for termux users (JSON) !
    def list_termux(self):

        for data in self.dec(self.aes_key):

            all_data = {
                "site": data[0],
                "username": data[1],
                "password": data[2],
                "notes": data[3]
            }

            print(json.dumps(all_data, indent=3, ensure_ascii=False))

    def List(self):

        if self.os_obj.is_termux(): self.list_termux()
        else: self.list_linux()


    # change=false: get password for frist time
    # change=True: change the password
    def get_masster_password(self, change=False):

        if not change:

            print("[Sign up]\n")
            master_password = getpass.getpass("[$] Set Master Password: ")
            confirm_password = getpass.getpass("[$] Confirm Password: ")

            if master_password == confirm_password:

                hashed = bcrypt.hashpw(master_password.encode(), bcrypt.gensalt(self.rounds,self.prefix))
                
                self.insert_master(hashed)
                
                self.conn.commit()


            else:

                print("[!] Passwords do not match")
                sys.exit()


        elif change:

            master_password = getpass.getpass("[$] Set Master Password: ")
            confirm_password = getpass.getpass("[$] Confirm Password: ")

            if master_password == confirm_password:

                hashed = bcrypt.hashpw(master_password.encode(), bcrypt.gensalt(self.rounds,self.prefix))

                self.aes_key = self.e_obj.password_to_fernet_key(master_password, self.new_salt)

                
                return hashed

            else:

                print("\n[!] Passwords do not match\n")
                self.menu()


    # get master password bcrypt hash from the database!
    def get_master_hash(self):

        for data in self.c.execute("SELECT password FROM master;"):
            return data[0]


    # get the salt from the database
    def get_salt(self):

        try: salt = self.c.execute("SELECT salt FROM master;").fetchall()[0][0]; return salt

        except: pass


    # check if hash exists in the database!
    def check_if_hash_exists(self):

        if self.get_master_hash(): return True

        else: return False


    # Compare the password with the hash in the database
    def check_hash(self, password):

        hashed = bcrypt.hashpw(password.encode(), self.get_master_hash().encode())

        if hashed.decode() == self.get_master_hash(): return True

        else: return False



    # double_check=False: Lgoin into program
    # doubl_check=True: check for master privileges
    def master_login(self, double_check=False):
        

        if not double_check:

            print("[login]\n")

            password = getpass.getpass("[$] Enter Master Password: ")

            self.aes_key = self.e_obj.password_to_fernet_key(password, self.salt)

            if self.check_hash(password): self.clear(); Banner(); self.menu()

            else: print("password incorrect!"); sys.exit()
                

        elif double_check:
            
            password = getpass.getpass("[$] Enter Master Password: ")

            self.aes_key = self.e_obj.password_to_fernet_key(password, self.salt) 

            self.old_aes_key = self.e_obj.password_to_fernet_key(password, self.salt) 

            if self.check_hash(password): return True

            else: print("\npassword incorrect!\n"); self.menu()


                
    # change master password
    def change_master_password(self, hash, salt):
        
        self.c.execute(f"UPDATE master SET password = '{str(hash)}', salt = '{str(salt)}';")

        data = self.dec(self.old_aes_key)

        self.c.execute("DROP TABLE data;"); self.conn.commit()
        self.create_data_tb()
        
        for i in data:

            #print(i)

            encrypted_data = self.e_obj.encrypt(i, self.aes_key)

            self.insert_into_data(
                encrypted_data[0],
                encrypted_data[1],
                encrypted_data[2],
                encrypted_data[3]
            )

        self.conn.commit()


    # ask user for input data
    def input_data(self):

        self.clear(); Banner()

        site = self.i_obj.site_input()
        username = self.i_obj.username_input()
        password, choice = self.i_obj.password_input()

        if choice == "y": print(f"[$] Your Password is: {password}")
        
        note = self.i_obj.notes_input()

        encrypted_data = self.e_obj.encrypt([
            site, username, 
            password, note], self.aes_key)

        self.insert_into_data(
            encrypted_data[0],
            encrypted_data[1],
            encrypted_data[2],
            encrypted_data[3]
        )

        self.clear(); Banner()

    # main menu 
    def menu(self):

        
        print("[1] - Add password")
        print("[2] - List all")
        print("[3] - Generate Password")
        print("[4] - Change Master Password")
        print("[X] - Exit")

        inp = input(">> ")

        while True:

            if inp == "1":
                self.input_data()
                self.menu()

            elif inp == "2":
                self.clear(); Banner()
                self.master_login(True); self.List(); self.menu()
                

            elif inp == "3":

                length = self.i_obj.input_length()

                print(f"\n[$] Your password is: {self.e_obj.gen_strong_password(length)}\n")

                self.menu()

            elif inp == "4":

                if self.master_login(True): 

                    password = self.get_masster_password(True)
                    self.change_master_password(password.decode(), self.new_salt)
                    print("Password Changed successfully, Try login !"); sys.exit()

                
            elif str(inp).lower() == 'x':

                print("bye !"); sys.exit()

            else:
                print(f"[!] incorrect command")
                inp = input(">> ")


if __name__ == "__main__":


    d_obj = DB()
