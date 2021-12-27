import tkinter as tk

def send_info():
    submission = entry.get()
    
window = tk.Tk()

window.title("Spanish-English Dictionary")
window.configure(background="#F5B31E")

label = tk.Label(text="Type in a Spanish or English word")
entry = tk.Entry()
button = tk.Button(text="enter")
label.grid(row=0, column = 0, columnspan=2, pady = 5)
entry.grid(row=1, column = 0, pady = 5)
button.grid(row=1, column = 1, sticky="W", command=send_info)
window.mainloop()

