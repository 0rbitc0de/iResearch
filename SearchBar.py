from tkinter import *
import wikipedia


def get_me():
    entry_value = entry.get()
    answer.delete(1.0, END)
    try:
        answer_value = wikipedia.summary(entry_value)
        answer.insert(INSERT, answer_value)
    except:
        answer.insert(INSERT, "please check you input or internet connection")


root = Tk()

root.geometry("500x500")
root.configure(bg="beige")
root.title("Search Bar - GUI")

label_1 = Label(root, text="iResearch")
label_1.pack()

topframe = Frame(root)
entry = Entry(topframe)
entry.pack()
button = Button(topframe, text="search", command=get_me)
button.pack()
topframe.pack(side = TOP)


bottomframe = Frame(root)
scroll = Scrollbar(bottomframe)
scroll.pack(side=RIGHT, fill=Y)
answer =  Text(bottomframe, width=50, height=17, yscrollcommand = scroll.set, wrap=WORD)
scroll.config(command=answer.yview)
answer.pack()
bottomframe.pack()

root.mainloop()
