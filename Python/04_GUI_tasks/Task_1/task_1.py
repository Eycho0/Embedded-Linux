import tkinter as tk

def toggle_led():
    global led_state
    if led_state:
        canvas.itemconfig(led, fill="grey")
    else:
        canvas.itemconfig(led, fill="red")
    led_state = not led_state

app = tk.Tk()
app.title("LED")
app.geometry("300x200")

led_state = False

canvas = tk.Canvas(app, width=100, height=100)
canvas.pack(pady=20)

led = canvas.create_oval(20, 20, 80, 80, fill="grey")

button = tk.Button(app, text="Toggle LED", command=toggle_led)
button.pack()

app.mainloop()
