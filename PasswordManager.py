import Encryption as en
import json
import os

class PasswordManager:
    def __init__(self,password_file="passwords.json"):
        self.password_file = password_file
        self.passwords = {}
        self.encryption = en.Encryption()
        self.load_passwords()
    
    
    def load_passwords(self): # loads the passwords from the json file
        if os.path.exists(self.password_file):
            try:
                with open(self.password_file, "r") as file:
                    self.passwords = json.load(file)
            except (json.JSONDecodeError, FileNotFoundError):
                print("Error")
                self.passwords = {}      
        else:
            print("No passwords found")
            
    def save_passwords(self): # saves the passwords to the json file
        with open(self.password_file, "w") as file:
            json.dump(self.passwords, file) 
        
        
    def add_password(self, service, password):
        self.passwords[service] = self.encryption.encrypt_password(password).decode()  # Convert bytes to string for JSON
        self.save_passwords()

         
    def view_passwords(self):  # Shows all services with their passwords
        if not self.passwords:
            return "No passwords stored."
        
        result = "Stored passwords:\n"
        for service, encrypted_password in self.passwords.items():
            try:
                decrypted_password = self.encryption.decrypt_password(encrypted_password.encode())
                result += f"{service}: {decrypted_password}\n"
            except Exception:
                result += f"{service}: Error decrypting password\n"
        return result

    
    
    def view_all_services(self): # returns all the services
        services = ""
        for service in self.passwords.keys():
            services += service + " , "
        return services.strip()
        
    
    def delete_password(self, service):
        if service in self.passwords:
            del self.passwords[service]
            self.save_passwords()
            return f"Successfully deleted password for {service}."
        else:
            return "Service not found."



        
        

