import tkinter as tk
from math import factorial

def calculate_factorial():
    num = int(entry.get())
    result = factorial(num)
    result_label.config(text=f"The factorial of {num} is {result}")

root = tk.Tk()
root.title("Factorial")
root.geometry("300x300")
root.resizable(False, False)

label = tk.Label(root, text="Enter a number:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Calculate Factorial", command=calculate_factorial)
button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
