import tkinter as tk
from tkinter import messagebox
from cnp import CNP, Persoana, MainFunction
from insertdb2 import MainInsert, InvalidInsert
import checkdatabase

class TK:
    def __init__(self, root):
        self.root = root
        self.function_register_ran = False
        self.message = ' '
        
        # Create and configure the form frame
        self.form_frame = tk.Frame(root, padx=10, pady=10)
        self.form_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Create and pack labels and entry widgets for name, surname, and CNP
        tk.Label(self.form_frame, text="Name:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.name_entry = tk.Entry(self.form_frame)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.form_frame, text="Surname:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.surname_entry = tk.Entry(self.form_frame)
        self.surname_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.form_frame, text="CNP:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        self.cnp_entry = tk.Entry(self.form_frame)
        self.cnp_entry.grid(row=2, column=1, padx=10, pady=5)

        # Create and configure the registration button
        tk.Button(self.form_frame, text="CNP validation", command=self.register).grid(row=3, column=0, padx=10, pady=5)

        # Create and configure the add button
        tk.Button(self.form_frame, text="Add to database", command=self.add_function).grid(row=3, column=1, padx=10, pady=5)

        # Create and configure the reset button
        tk.Button(self.form_frame, text="Reset", command=self.reset_form).grid(row=4, column=0, columnspan=2, pady=10)


    def register(self):
        name = self.name_entry.get()
        surname = self.surname_entry.get()
        cnp = self.cnp_entry.get()        

        # Validate CNP
        if not any(char.isdigit() for char in cnp):
            messagebox.showwarning("Input Error", "CNP invalid - must contain only numeric!")
            return

        # Validate input
        if not name or not surname or not cnp:
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        # Create Persoana object and validate
        persoana1 = Persoana(cnp, name, surname)
        self.message = MainFunction.show_details_for_person(persoana1)

        # Show success message
        messagebox.showinfo("Validation Successful", self.message) 
        self.function_register_ran = True

    def add_function(self):
        name = self.name_entry.get()
        surname = self.surname_entry.get()
        cnp = self.cnp_entry.get()

        # Warning message if the validation button wasn t pressed 
        if self.function_register_ran == False:
            messagebox.showwarning("Please Validate", "Please press the - CNP validation - button!")
            return

        # Validate input
        if not name or not surname or not cnp:
            messagebox.showwarning("Input Error", "All fields are required!")
            return 
        
        # Validate CNP
        if not any(char.isdigit() for char in cnp):
            messagebox.showwarning("Input Error", "CNP invalid - must contain only numeric!")
            return

        # Check if present into db2
        try:
            user = MainInsert(name, surname, cnp, self.message)
            user.insert_data()
            messagebox.showinfo("Add Successful", "Successfully added to database")
        except InvalidInsert as e:
            messagebox.showwarning("DB2 error", "Insert error - CNP already present in DB2")
        except Exception as e:
            messagebox.showwarning("DB2 error", "Insert error - CNP already present or other database error")
        
    def reset_form(self):
        # Clear all entry widgets
        self.name_entry.delete(0, tk.END)
        self.surname_entry.delete(0, tk.END)
        self.cnp_entry.delete(0, tk.END)
        
        # Optionally set focus to the name_entry
        self.name_entry.focus_set()



# Create main window
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x250")
    root.title("Registration Form")

    # Set the window's background
    root.configure(background="yellow")

    # Create an instance of the TK class
    app = TK(root)

    # Run the Tkinter main loop
    root.mainloop()