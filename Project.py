from tkinter import Tk,Entry,Button,Label,StringVar

window=Tk()
window.geometry("400x150")
window.title("Hebrew Dictionary")
entry_text= Entry(window)
entry_text.pack()

result=StringVar()
result_label=Label(window,textvariable=result)
result_label.pack()

hebrew_dictionary={
    "shalom":"hello",
    "sefer":"book",
    "ochel":"food",
    "mayim":"water",
    "khise":"chair",
    "ken":"yes",
    "lo":"no",
    "toda":"thank you",
    "bevakasha":"please",
    "slicha":"sorry",
    "bayit":"house",
    "chaver":"friend",
    "yom":"day",
    "laila":"night",
    "kesef":"money",
    "lev":"heart",
    "tov":"good",
    "ra":"bad",
    "yav":"beautiful",
    "rosh":"head",
    "ahavah":"love",
    "gadol":"big",
    "katan":"small",
    "olam":"world",
    "esh":"fire",
    "yam":"sea",
    "ohr":"light",
    "shulchan":"table",
    "begadim":"clothes",
    "sababa":"great"
}

def search(word):
    if word in hebrew_dictionary:
        result.set(hebrew_dictionary[word])
        print(hebrew_dictionary[word])

    else:
        result.set("Not found")
        print("Not found")


search_btn=Button(window,text="Search", command=lambda: search(entry_text.get()))
search_btn.pack()
window.mainloop()
