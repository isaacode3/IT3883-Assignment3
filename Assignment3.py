# Program Name: Assignment3.py
# Course: IT3883/Section 01
# Student Name: Isaac Odeyemi
# Assignment Number: Lab3
# Due Date: 02/23/2026
# Purpose: This program converts Miles per Gallon (MPG) into Kilometers per Liter (KM/L)
#          using a graphical user interface (GUI). The conversion updates automatically
#          as the user types, without needing to press a button.
# Resources: Class notes, Python documentation, Tkinter documentation

import tkinter as tk


# -----------------------------
# Function to perform conversion
# -----------------------------
def convert_mpg_to_kml(event=None):
    """
    This function is called every time the user types in the entry box.
    It converts MPG to KM/L and updates the result label.
    """

    user_input = mpg_entry.get()

    try:
        # Attempt to convert input to float
        mpg = float(user_input)

        # Conversion formula
        kml = mpg * 0.425143707

        # Update result with 4 decimal places
        result_var.set(f"{kml:.4f} km/L")

    except ValueError:
        # If input is invalid (letters, blank, etc.), clear result
        result_var.set("")


# -----------------------------
# Create main window
# -----------------------------
root = tk.Tk()
root.title("MPG to KM/L Converter")
root.geometry("350x180")


# -----------------------------
# Create labels and entry field
# -----------------------------
title_label = tk.Label(root, text="MPG to KM/L Converter",
                       font=("Arial", 14, "bold"))
title_label.pack(pady=10)

mpg_label = tk.Label(root, text="Enter MPG:")
mpg_label.pack()

# Entry box for MPG input
mpg_entry = tk.Entry(root, width=20)
mpg_entry.pack()

# Bind key release event so conversion happens while typing
mpg_entry.bind("<KeyRelease>", convert_mpg_to_kml)


# -----------------------------
# Result display
# -----------------------------
result_var = tk.StringVar()

result_label = tk.Label(root,
                        textvariable=result_var,
                        font=("Arial", 12),
                        fg="blue")
result_label.pack(pady=15)


# -----------------------------
# Run the GUI loop
# -----------------------------
root.mainloop()