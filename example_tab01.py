from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText


def demo():
    root = tk.Tk()
    root.title("tab")

    nb = ttk.Notebook(root)

    page1 = ttk.Frame(nb)

    page2 = ttk.Frame(nb)
    text = ScrolledText(page2)
    text.pack(expand=1, fill="both")

    nb.add(page1, text='One')
    nb.add(page2, text='Two')

    nb.pack(expand=1, fill="both")

    root.mainloop()

if __name__ == "__main__":
    demo()