import tkinter as tk
from tkinter import ttk
from dictionary import SearchBot
import sqlite3

def send_info():
    submission = str(entry.get())
    search_bot = SearchBot(submission)
    
    # Databases
    # Create a database or connect to one
    conn = sqlite3.connect('es_dictionary.db')
    # create cursor
    c = conn.cursor()
    
    # Query the database
    #c.execute("SELECT * FROM words WHERE word_name = ?", str(entry.get()))
    
    
    c.execute("SELECT * FROM words WHERE word_name = ?", [submission])
    # print(c.fetchone())
    
    
    #search_bot = SearchBot(submission)
    
    if c.fetchone() is None:
        search_bot.search_query()
        #print(search_bot.grammar_dict)
        message = search_bot.output_message()
        c.execute("INSERT INTO words VALUES (:word_name, :definition)", {'word_name':search_bot.query, 'definition': message})
    else:
        c.execute("SELECT * FROM words WHERE word_name = ?", [submission])
        message = c.fetchone()[1]
        
    # search_bot.display_info()
    
    # commit changes
    conn.commit()
    # close connection
    conn.close()
    
    
    newWindow = tk.Toplevel(window)
    
    newWindow.title("Word")
    #tk.Label(newWindow, text = search_bot.query).pack()
    
    
    text_box = tk.Text(newWindow, height=39, width=120, wrap='word')
    text_box.pack(padx=20, side=tk.LEFT, expand=True)
    text_box.insert(tk.END, message)
    
    sb = tk.Scrollbar(newWindow)
    
    sb.pack(side=tk.RIGHT, fill=tk.BOTH)
    text_box.config(yscrollcommand=sb.set)
    sb.config(command=text_box.yview)
     

def return_words():
    conn = sqlite3.connect('es_dictionary.db')
    c = conn.cursor()
    c.execute("SELECT * from words")
    
    message = ""
    for word, definition in c.fetchall():
        message += (word + "\n")
    #print(c.fetchall())
    
    returnWindow = tk.Toplevel(window)
    returnWindow.title("Words")
    
    text_box = tk.Text(returnWindow, wrap='word')
    text_box.pack(expand=True)
    text_box.insert(tk.END, message)
    
    
    
    
window = tk.Tk()

window.iconbitmap("crayons.ico")
window.title("Spanish-English Dictionary")
window.configure(background="#F5B31E")

label = tk.Label(text="Type in a Spanish or English word")
entry = tk.Entry()
button = tk.Button(text="enter", command=send_info)
label.grid(row=0, column = 0, columnspan=2, pady = 5)
entry.grid(row=1, column = 0, pady = 5)
button.grid(row=1, column = 1, sticky="W")

# This is the button to return words in the database
separator = ttk.Separator(window, orient='horizontal')
separator.grid(row=2, sticky="EW", pady = 5, columnspan=2)
past_word_btn = tk.Button(text="previous words", command=return_words)
past_word_btn.grid(row=3, column = 0, sticky="W", padx = 5, pady = (0, 5))

"""
conn = sqlite3.connect('es_dictionary.db')
c = conn.cursor()
# create table
c.execute("CREATE TABLE words (word_name text,definition text)")
conn.commit()
conn.close()
"""
          

window.mainloop()

