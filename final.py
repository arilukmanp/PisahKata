from tkinter import *
from math import log

root = Tk()
root.geometry('400x300')
root.title("Pisah Kata")
root.configure(background='#009688')

words = open("kamus_data.txt").read().split()
wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
maxword = max(len(x) for x in words)

def pisah(s):

    # Mencari karakter yg sesuai, lalu mengembalikan nilai kata yg sesuai & panjang karakter
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    out = []
    i = len(s)
    while i>0:
        c,k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k

    return " ".join(reversed(out))

def buttonclick():
	result.delete('1.0', END)
	input = entry.get("1.0",END)
	result.insert(END, pisah(input))

lbl = Label(root, text="Kalimat Yang Ingin Dipisah:", background="#009688", foreground="#fff")
lbl.place(x=125, y=20)

entry = Text(root, width=47, height=3)
entry.place(x=10, y=43)

button = Button(root, text="Pisahkan Kata", command=buttonclick, background="#0B31C4", foreground="#fff")
button.place(x=160, y=130)

lbl2 = Label(root, text="Hasil Kalimat:", background="#009688", foreground="#fff")
lbl2.place(x=163, y=188)

result = Text(root, width=47, height=3)
result.place(x=10, y=210)


root.mainloop()