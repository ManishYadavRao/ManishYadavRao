import tkinter as tk
import re

def password_strength(password):
    # Criteria for a strong password
    length_criteria = len(password) >= 8
    upper_case_criteria = re.search(r'[A-Z]', password) is not None
    lower_case_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None
    
    # Calculate strength based on criteria met
    strength = sum([length_criteria, upper_case_criteria, lower_case_criteria, digit_criteria, special_char_criteria])
    
    # Determine password strength level
    if strength == 5:
        return "Very Strong"
    elif strength == 4:
        return "Strong"
    elif strength == 3:
        return "Moderate"
    elif strength == 2:
        return "Weak"
    else:
        return "Very Weak"

def check_password_strength():
    password = password_entry.get()
    strength = password_strength(password)
    result_label.config(text=f"Password Strength: {strength}")

# Set up the GUI
root = tk.Tk()
root.title("Password Strength Checker")

# Create and place the widgets
password_label = tk.Label(root, text="Enter your password:")
password_label.pack()

password_entry = tk.Entry(root, show='*')
password_entry.pack()

check_button = tk.Button(root, text="Check Strength", command=check_password_strength)
check_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()
