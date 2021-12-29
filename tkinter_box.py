import tkinter as tk
from dictionary import SearchBot

def send_info():
    submission = str(entry.get())
    search_bot = SearchBot(submission)
    search_bot.search_query()
    search_bot.display_info()
    
    newWindow = tk.Toplevel(window)
    
    newWindow.title("Word")
    tk.Label(newWindow, text = "this is a new window").pack()
    
    message = search_bot.output_message()
    text_box = tk.Text(newWindow, height=39, width=120, wrap='word')
    text_box.pack(padx=20, side=tk.LEFT, expand=True)
    text_box.insert(tk.END, message)
    
    sb = tk.Scrollbar(newWindow)
    
    sb.pack(side=tk.RIGHT, fill=tk.BOTH)
    text_box.config(yscrollcommand=sb.set)
    sb.config(command=text_box.yview)
    
window = tk.Tk()

window.title("Spanish-English Dictionary")
window.configure(background="#F5B31E")

label = tk.Label(text="Type in a Spanish or English word")
entry = tk.Entry()
button = tk.Button(text="enter", command=send_info)
label.grid(row=0, column = 0, columnspan=2, pady = 5)
entry.grid(row=1, column = 0, pady = 5)
button.grid(row=1, column = 1, sticky="W")
window.mainloop()

