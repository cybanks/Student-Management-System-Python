import tkinter as tk
from tkinter import messagebox

# Author: Ankit Shukla
# Student Management System with Dark Theme

class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("600x400")
        
        # Apply Dark Theme
        self.root.configure(bg="#1e1e1e")  # Dark Background
        self.text_color = "#ffffff"  # White Text
        
        # Student Data Storage
        self.students = []
        
        # Labels
        self.label_title = tk.Label(root, text="Student Management System", font=("Arial", 16, "bold"), fg=self.text_color, bg="#1e1e1e")
        self.label_title.pack(pady=10)
        
        self.label_name = tk.Label(root, text="Student Name:", fg=self.text_color, bg="#1e1e1e")
        self.label_name.pack()
        
        self.entry_name = tk.Entry(root)
        self.entry_name.pack()
        
        self.label_age = tk.Label(root, text="Age:", fg=self.text_color, bg="#1e1e1e")
        self.label_age.pack()
        
        self.entry_age = tk.Entry(root)
        self.entry_age.pack()
        
        # Buttons
        self.button_add = tk.Button(root, text="Add Student", command=self.add_student, bg="#444", fg=self.text_color)
        self.button_add.pack(pady=5)
        
        self.button_view = tk.Button(root, text="View Students", command=self.view_students, bg="#444", fg=self.text_color)
        self.button_view.pack(pady=5)
        
        self.button_exit = tk.Button(root, text="Exit", command=root.quit, bg="#ff5555", fg=self.text_color)
        self.button_exit.pack(pady=5)
    
    def add_student(self):
        """Function to add a student to the list"""
        name = self.entry_name.get()
        age = self.entry_age.get()
        
        if name and age.isdigit():
            self.students.append({"name": name, "age": int(age)})
            messagebox.showinfo("Success", f"Student {name} added successfully!")
            self.entry_name.delete(0, tk.END)
            self.entry_age.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a valid name and age.")
    
    def view_students(self):
        """Function to display all students"""
        if not self.students:
            messagebox.showinfo("No Students", "No students added yet!")
            return
        
        students_info = "\n".join([f"{s['name']} (Age: {s['age']})" for s in self.students])
        messagebox.showinfo("Student List", students_info)

# Run the Application
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
