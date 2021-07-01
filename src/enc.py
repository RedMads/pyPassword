# This file for Encrypt, Decrypt !


from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
from base64 import urlsafe_b64encode
import string, random


#This class for encrypt functions!
class Encrypt:

    def __init__(self):

        self.symbols = "!@#$%^&*"
        self.chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + self.symbols


        self.L = False; self.U = False 
        self.N = False; self.S = False
        
        
    # convert string password to fernet key!
    def password_to_fernet_key(self, password, salt):


        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt= salt.encode(),
            iterations=100000,
        )


        return urlsafe_b64encode(kdf.derive(password.encode("utf-8")))


    # Encrypt function !
    def encrypt(self, data:list, key):

        cipher = Fernet(key)

        enc = []

        for d in data:

            encrypted_data = cipher.encrypt(d.encode())

            enc.append(encrypted_data.decode())

        return enc

    # Decrypt function !
    def decrypt(self, enc_data:list, key):

        cipher = Fernet(key)

        dec = []

        for d in enc_data:

            decrypted_data = cipher.decrypt(d.encode())

            dec.append(decrypted_data.decode())

        return dec


    # Generate string function !
    def generator(self,length= 30):


        STR = []

        for _ in range(length):

            STR.append(random.choice(self.chars))

        full_str = "".join(STR)

        return full_str


    # strong password function check!
    def gen_strong_password(self, length=30):

        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        numbers = string.digits
        symbols = self.symbols
        run = True

        while run:

            password = self.generator(length)

            for i in lowercase: 

                if i in password: self.L = True

            for j in uppercase:

                if j in password: self.U = True

            for k in numbers:

                if k in password: self.N = True

            for l in symbols:

                if l in password: self.S = True


            if (
                self.L == True and self.U == True and 
                self.N == True and self.S == True
            ): run = False; return password

            else: run = True; password = self.generator(length)

# Just For Test !
if __name__ == "__main__":

    e_obj = Encrypt()

    
    encrypted = e_obj.encrypt(["Hello","World","!"], e_obj.password_to_fernet_key("password123"))


    for e in encrypted:

        print(e)


    decrypted = e_obj.decrypt(encrypted, e_obj.password_to_fernet_key("password123"))


    for d in decrypted:

        print(d)

    print(e_obj.generator(30))

    print(e_obj.generator(30,True))
