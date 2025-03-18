from cryptography.fernet import Fernet
import os



class Encryption:
    def __init__(self,key_file="key.key"):
        self.key_file = key_file
        self.key = self.load_key()  
        self.cipher = Fernet(self.key)  
        
        
    def load_key(self):
        if os.path.exists(self.key_file):
            with open(self.key_file, "rb") as file:
                return file.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, "wb") as file:
                file.write(key)
            return key
        
    def encrypt_password(self, password):
        return self.cipher.encrypt(password.encode())

    
    def decrypt_password(self, password):
        return self.cipher.decrypt(password).decode()
