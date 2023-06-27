import tkinter
from tkinter import scrolledtext
import logging
from fts.indexing import Indexing
from fts.ftsearch import Ftsearch
from nlp.words import Words


root = tkinter.Tk()
root.title("chatbot")
root.geometry("405x230")
root.configure(bg = "black")

llist = []
rlist = []
dlist = []

with open("./data/chatbot-data.txt", "r") as file:
    for line in file:
        if not line:
            continue
        else:
            left, right, *res = line.split(":")
            llist.append(left)
            rlist.append(right.replace("\n", ""))

# tokenize sentences to words
for i in llist:
    tokword = Words(i)
    tokwordload = tokword.load()
    dlist.append(tokwordload)

memo = Indexing(dlist)
fmemo = memo.load()

def send():
    xlist = []
    reply = "Chatbot: more information..\n"
    user = "User: " + ent.get() + "\n"
    txt.insert(tkinter.END, user)
    logging.info(user.replace("\n", ""))
    if not ent.get():
        pass
    else:
        word = Words(ent.get())
        wordload = word.load()
        ent.delete(0, "end")
        for i in wordload:
            if i not in xlist:
                xlist.append(i)
        var = Ftsearch(xlist, fmemo)
        xvar = var.load()
        for i in xvar.items():
            c, k = i
            if len(wordload) <= k:
                if len(wordload) * 100 / len(dlist[c]) == 100:
                   reply = "Chatbot: " + rlist[c] + "\n"
        txt.insert(tkinter.END, reply)
        logging.info(reply.replace("\n", ""))


ent = tkinter.Entry(root, width = 40)
ent.focus()
btn1 = tkinter.Button(root, text = "send", bg = "gray", command = send)
txt = scrolledtext.ScrolledText(root, width = 45, height = 10)
txt.grid(column = 0, row = 0)
ent.place(x = 5, y = 190 )
btn1.place(x = 340, y = 185)

logging.basicConfig( level=logging.DEBUG, filename = "mylog.log", filemode="a", format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s", datefmt='%H:%M:%S')

if __name__ == "__main__":
    root.mainloop()
