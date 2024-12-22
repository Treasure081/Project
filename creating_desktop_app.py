from tkinter import Tk, Entry, Button, Label, StringVar

#creating a window...

window = Tk()

#width and length of window
window.geometry("600x250")

window.title("Tiv Dictionary")

entry_text =Entry(window)
entry_text.pack()

result=StringVar()
result_label=Label(window,textvariable=result)
result_label.pack()

tiv_dictionary={
    "kwaghyan":"food",
    "hunda":"door",
    "gbenda":"road",
    "yem":"go",
    "va":"come",
    "kujera":"stool",
    "usu":"light",
    "guwa":"leg",
    "ashe":"eyes",
    "zwa":"mouth"
}



def search(word):
    if word in tiv_dictionary:
        result.set(tiv_dictionary[word])
        print(tiv_dictionary[word])

    else:
        result.set("Not found")
        print("Not found")


search_btn=Button(window,text="Search", command=lambda: search(entry_text.get()))
search_btn.pack()
window.mainloop()