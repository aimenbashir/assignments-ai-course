import tkinter as tk
from tkinter import messagebox
import numpy as np

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "Addition":
            result = np.add(num1, num2)
        elif operation == "Subtraction":
            result = np.subtract(num1, num2)
        elif operation == "Multiplication":
            result = np.multiply(num1, num2)
        elif operation == "Division":
            if num2 != 0:
                result = np.divide(num1, num2)
            else:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
        else:
            messagebox.showerror("Error", "Please select a valid operation!")
            return

        result_label.config(text=f"Result: {result}")
    
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

# Setting up the Tkinter window
window = tk.Tk()
window.title("Simple Calculator")

# User input fields
entry1 = tk.Entry(window, width=10)
entry1.grid(row=0, column=1, padx=10, pady=10)

entry2 = tk.Entry(window, width=10)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Labels for the input fields
label1 = tk.Label(window, text="First Number:")
label1.grid(row=0, column=0, padx=10, pady=10)

label2 = tk.Label(window, text="Second Number:")
label2.grid(row=1, column=0, padx=10, pady=10)

# Dropdown for selecting the operation
operation_var = tk.StringVar(window)
operation_var.set("Select Operation")

operation_menu = tk.OptionMenu(window, operation_var, "Addition", "Subtraction", "Multiplication", "Division")
operation_menu.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Result label
result_label = tk.Label(window, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Running the main loop
window.mainloop()
