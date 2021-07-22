from tkinter import Tk, Entry, Label, Button

def press():
    print("poulstar")


main = Tk()

main.geometry('320x240')

Label(main, text="Name : ").pack()
Entry(main).pack()
Button(main, text="Click", command=press).pack()



main.mainloop()