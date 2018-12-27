try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *
from math import log

root = Tk()
root.geometry('400x300')
root.title("Pisah Kata")
root.configure(background='#009688')

DICTIONARY_OPTIONS = [
    "kamus_en.txt",
    "kamus_id.txt"
]
dictionaryVariable = StringVar(root)
dictionaryVariable.set(DICTIONARY_OPTIONS[0])

def get_dictionary():
    return dictionaryVariable.get()

words = open(get_dictionary()).read().split()
word_cost = dict((k, log((i + 1) * log(len(words)))) for i, k in enumerate(words))
max_word = max(len(x) for x in words)

def reload_dictionary(*args):
    global words
    words = open(get_dictionary()).read().split()
    global word_cost
    word_cost = dict((k, log((i + 1) * log(len(words)))) for i, k in enumerate(words))
    global max_word
    max_word = max(len(x) for x in words)



def pisah(string):
    # Buang semua karakter non-alfanumerik
    string = re.sub('\W+', '', string)

    # Mencari karakter yg sesuai, lalu mengembalikan nilai kata yg sesuai & panjang karakter
    def best_match(index):
        candidates = enumerate(reversed(cost[max(0, index - max_word):index]))
        return min((c + word_cost.get(string[index - k - 1:index], 9e999), k + 1) for k, c in candidates)

    cost = [0]
    for i in range(1, len(string) + 1):
        c, k = best_match(i)
        cost.append(c)

    out = []
    i = len(string)
    while i > 0:
        c, k = best_match(i)
        assert c == cost[i]
        out.append(string[i - k:i])
        i -= k

    return " ".join(reversed(out))


def buttonclick():
    result.delete('1.0', END)
    input = entry.get("1.0", END)
    result.insert(END, pisah(input))


lbl = Label(root, text="Kalimat Yang Ingin Dipisah:", background="#009688", foreground="#fff")
lbl.place(x=125, y=20)

entry = Text(root, width=47, height=3)
entry.place(x=10, y=43)

option = apply(OptionMenu, (root, dictionaryVariable) + tuple(DICTIONARY_OPTIONS))
option.place(x=40, y=130)
dictionaryVariable.trace('w', reload_dictionary)

button = Button(root, text="Pisahkan Kata", command=buttonclick, background="#0B31C4", foreground="#fff")
button.place(x=200, y=130)

lbl2 = Label(root, text="Hasil Kalimat:", background="#009688", foreground="#fff")
lbl2.place(x=163, y=188)

result = Text(root, width=47, height=3)
result.place(x=10, y=210)

root.mainloop()
