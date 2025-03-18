import tkinter as tk
from tkinter import messagebox
import PasswordManager as pm


class PasswordManagerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")
        self.master.geometry("400x400")
        
        self.password_manager = pm.PasswordManager()
        
        self.create_widgets()
    
    def create_widgets(self):
        # Add service and password
        self.service_label = tk.Label(self.master, text="Service:")
        self.service_label.pack()
        
        self.service_entry = tk.Entry(self.master)
        self.service_entry.pack()
        
        self.password_label = tk.Label(self.master, text="Password:")
        self.password_label.pack()
        
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack()
        
        self.add_button = tk.Button(self.master, text="Add Password", command=self.add_password)
        self.add_button.pack()
        
        # View passwords
        self.view_button = tk.Button(self.master, text="View Passwords", command=self.view_passwords)
        self.view_button.pack()
        
        self.delete_label = tk.Label(self.master, text="Delete Service:")
        self.delete_label.pack()
        
        self.delete_entry = tk.Entry(self.master)
        self.delete_entry.pack()
        
        self.delete_button = tk.Button(self.master, text="Delete Password", command=self.delete_password)
        self.delete_button.pack()

        # Quit button
        self.quit_button = tk.Button(self.master, text="Quit", command=self.master.quit)
        self.quit_button.pack()
    
    def add_password(self):
        service = self.service_entry.get()
        password = self.password_entry.get()
        
        if service and password:
            self.password_manager.add_password(service, password)
            messagebox.showinfo("Success", f"Password for {service} added.")
            self.service_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Both service and password must be provided.")
    
    def view_passwords(self):
        passwords = self.password_manager.view_passwords()
        if passwords == "No passwords stored.":
            messagebox.showinfo("No Passwords", passwords)
        else:
            self.show_text_popup("Stored Passwords", passwords)
    
    def delete_password(self):
        service = self.delete_entry.get()  # Get the service name from the input field
        
        if service:  # Check if the service field is not empty
            result = self.password_manager.delete_password(service)  # Call the delete method from PasswordManager
            
            if "Successfully deleted" in result:  # If the result contains success
                messagebox.showinfo("Success", result)
            else:
                messagebox.showwarning("Service Not Found", result)
            
            # Clear the input field after the operation
            self.delete_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please provide a service to delete.")


    def show_text_popup(self, title, text):
        popup = tk.Toplevel(self.master)
        popup.title(title)
        popup.geometry("400x400")
        
        text_box = tk.Text(popup, wrap=tk.WORD)
        text_box.insert(tk.END, text)
        text_box.pack(expand=True, fill=tk.BOTH)
        
        close_button = tk.Button(popup, text="Close", command=popup.destroy)
        close_button.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManagerGUI(root)
    root.mainloop()
