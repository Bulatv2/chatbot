import tkinter
from tkinter import scrolledtext

root = tkinter.Tk()
root.title("chatbot gui")
root.geometry("405x230")
root.configure(bg = "black")

def send():
    pass

ent = tkinter.Entry(root, width = 40)
ent.focus()
btn1 = tkinter.Button(root, text = "send", bg = "gray", command = send)
txt = scrolledtext.ScrolledText(root, width = 45, height = 10)
txt.grid(column = 0, row = 0)
ent.place(x = 5, y = 190 )
btn1.place(x = 340, y = 185)

if __name__ == "__main__":
    root.mainloop()
